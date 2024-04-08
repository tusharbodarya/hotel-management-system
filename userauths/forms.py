from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2')