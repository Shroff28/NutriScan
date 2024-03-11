from .forms import ReviewForm
from .models import Restaurant, User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    search_value = "test"
    # Filter according to name in search
    filtered_restaurants = restaurants.objects.filter(name__icontains=search_value)

    # Filter according to ratings
    rating_value = 1
    filtered_restaurants = filtered_restaurants.objects.filter(rating__gte=rating_value)

    # Filter according to Cuisine
    cuisine = []
    filtered_restaurants = filtered_restaurants.objects.filter(cuisine__in=cuisine).all()

    # TODO return proper template
    return ''


def temp_review_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    # TODO: Fetch user form request and add its ID
    user = get_object_or_404(User, pk=1)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = user
            review.save()
            return render(request, 'review_block.html', {'restaurant_id': restaurant_id, 'message': 'Review Submitted Successfully'})
    else:
        return render(request, 'review_block.html', {'review_from': form, 'restaurant_id': restaurant_id, 'restaurant_name': restaurant.name, 'message': ''})
