from django.contrib import admin
from django.db import models
from .models import User, UserProfile

# Register your models here.
admin.site.register(User)
#Registering model for User Setting
admin.site.register(UserProfile)

