from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logIn, name='logIn'),
    path('logout/', views.logOut, name='logOut'),
    path('signup/', views.signup, name='signUp'),
]