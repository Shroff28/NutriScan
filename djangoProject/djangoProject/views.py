from .forms import ReviewForm
from .models import Restaurant
from django.shortcuts import render
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


def temp_review_view(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return HttpResponseRedirect('')
    else:
        return render(request, 'review_block.html', {'review_from': form})
