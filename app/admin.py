from django.contrib import admin
from .models import *

# from .models import User, UserProfile, Review, Comment, Restaurant, MenuItem, Order, Cuisine

# # Register your models here.
# admin.site.register(User)

# # Registering model for User Setting
# admin.site.register(UserProfile)

# admin.site.register(Review)
# admin.site.register(Comment)
# admin.site.register(Restaurant)
# admin.site.register(MenuItem)
# admin.site.register(Order)


# @admin.register(Cuisine)
# class CuisineAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']

# =======================================================
# new fields
# =======================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id']