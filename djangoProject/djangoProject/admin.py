from django.contrib import admin
from .models import User, UserProfile, Review, Comment

# Register your models here.
admin.site.register(User)

# Registering model for User Setting
admin.site.register(UserProfile)

admin.site.register(Review)
admin.site.register(Comment)

