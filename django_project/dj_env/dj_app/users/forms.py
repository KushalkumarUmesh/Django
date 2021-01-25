from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # inbuilt form - KK
from .models import Profile

class UserRegistrationForm(UserCreationForm): #Creating new form:to have email field in addition to inbuilt view
    email=forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']