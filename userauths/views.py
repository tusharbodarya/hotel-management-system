from django.shortcuts import render

from userauths.models import User, Profile
from userauths.forms import UserRegisterForm

def RegisterView(request):
    form = UserRegisterForm()
    
    context = {
        "form": form,
    }
    
    return render(request, "userauths/register.html", context)