from pyexpat import model
from django.forms import widgets
from .models import SportAdvert,Profile, Wishlist,Sport,Comment,Location
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CoachRegistrationForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['first_name','last_name','email','username','password1','password2']

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control ','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }
