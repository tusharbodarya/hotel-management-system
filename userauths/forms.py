from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import FileInput
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter User Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone', 'email', 'password1', 'password2')
        
    
class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['email']
        
class ProfileUpdateFrom(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            "image",
            "full_name",
            "phone",
            "gender",
            "country",
            "city",
            "state",
            "address",
            "identity_type",
            "identity_image",
            "facebook",
            "twitter",
        ]
        
        widgets = {
            'image': FileInput(attrs={"onchange": "loadFile(event)", "class": "upload"})
            
            
        }