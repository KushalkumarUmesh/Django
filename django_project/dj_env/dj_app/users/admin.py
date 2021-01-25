#to register user models in admin site
from django.contrib import admin
from .models import Profile

#registering the Profile model to register
admin.site.register(Profile)