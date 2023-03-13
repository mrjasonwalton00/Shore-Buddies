from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #imports default user creation formn
from django import forms #imports django forms
from django.contrib.auth.models import User #uses the default django User model


#Form For User Registration
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) #takes in username
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) #takes in password
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) #confirmation password

    class Meta:
        model = User #based off django default User model
        fields = ['username', 'email', 'password1', 'password2']


