from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.urls import reverse


class SignUp(forms.Form):
    username = forms.CharField(label='Username', max_length=20, required=True)
    passwordOne = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput, required=True)
    passwordTwo = forms.CharField(label='Confirm Password', max_length=20, widget=forms.PasswordInput, required=True)
    email = forms.CharField(label = 'Email',max_length=50, required=True)


class LogIn(forms.Form):
    username = forms.CharField(label="Username", max_length=20, required=True)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput, required=True)
    
            

        
    