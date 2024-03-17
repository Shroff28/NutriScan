from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})
