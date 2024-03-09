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
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'review']

@admin.register(Restuarant)
class RestuarantAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone_number']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id']