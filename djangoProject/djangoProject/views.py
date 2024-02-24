from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render

from .models import User, UserProfile, Order, Restaurant, Cuisine, Menu, Payments, Review, Comment

def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    searchValue = "test"
    # Filter according to name in search
    filteredRestaurants = restaurants.objects.filter(name__icontains=searchValue)

    #Filter according to ratings
    ratingValue = 1
    filteredRestaurants = filteredRestaurants.objects.filter(rating__gte=1)

    # TODO return proper template
    return '';