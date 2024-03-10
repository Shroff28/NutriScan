from django.contrib import admin

from .models import User, UserProfile, Review, Restaurant, Cuisine

# Register your models here.
admin.site.register(User)

# Registering model for User Setting
admin.site.register(UserProfile)

admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(Review)
