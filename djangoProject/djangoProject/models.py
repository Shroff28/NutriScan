import uuid

from django.db import models
from djstripe.models import PaymentMethod


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cuisines = models.ManyToManyField(Cuisine)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    favorite_food = models.CharField(max_length=100, blank=True)
    favorite_restaurant = models.CharField(max_length=100, blank=True)

    # additional fields for user settings will be updated as per requirements

    def __str__(self):
        return self.user.username


class Menu:
    # TODO: Dhrumil
    pass


class Order(models.Model):
    # TODO: Jaydeep
    pass


class Payments(models.Model):
    payment_id = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment #{self.pk} for Order #{self.order_id}"


class Review(models.Model):
    RATINGS_RANGE = (
        (1, 'Poor'),
        (2, 'Bad'),
        (3, 'Mediocre'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    # timestamp to track when the review was given
    timestamp = models.DateTimeField(auto_now_add=True)
    # reference of the user who made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # reference of the restaurant the review was given to
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # rating given to the restaurant
    rating = models.IntegerField(default=0, choices=RATINGS_RANGE)
    # comment associated with the review
    comment = models.TextField(blank=True, null=True, help_text='Add your comment')

    class Meta:
        ordering = ["-timestamp"]
