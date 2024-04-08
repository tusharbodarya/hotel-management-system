from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter User Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone', 'email', 'password1', 'password2')