from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignUp, LogIn
from django.db.models import Max, Avg, Count

# Create your views here.
def index(request):
    return render(request, 'users/signup.html')

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            passwordOne = form.cleaned_data['passwordOne']
            passwordTwo = form.cleaned_data['passwordTwo']
            email = form.cleaned_data['email']

            if passwordOne != passwordTwo:
                return render(request, 'users/signup.html', {'form': form, 'error_message': "Passwords do not match."})

            else:
                user = User.objects.filter(username = username).aggregate(Count('username'))
                if user['username__count'] == 0:
                    if ' ' in username: 
                        return render(request, 'users/signup.html', {'form': form, 'error_message': "Username cannot contain spaces."})
                    else:
                        #Create the user
                        newUser = User.objects.create_user(username = username, password=passwordOne)
                        newUser.save()
                        

                        #Redirect to active waits
                        return HttpResponseRedirect(reverse('users:logIn'))

                else: 
                    return render(request, 'users/signup.html', {'form': form, 'error_message': "Username is already taken."})
                

                
    else:
        form = SignUp()       
            
            
    return render(request, 'users/signup.html', {'form': form})

def logIn(request):
    if request.method == "POST":
        form = LogIn(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            userAuth = authenticate(request, username = username, password = password)
            if userAuth is not None:
                login(request, userAuth)
                return HttpResponseRedirect(reverse('polls:index'))
            else:
                return render(request, 'users/login.html', {'form': form, "error_message": "Incorrect Username/Password"})

    else:
        form = LogIn()

    return render(request, 'users/login.html')

def logOut(request):
    if request.user.is_anonymous: 
        return HttpResponseRedirect(reverse('polls:index'))
    else: 
        logout(request)
        return HttpResponseRedirect(reverse('pages:index'))
    
