from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


