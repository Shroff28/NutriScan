from django.db import models
from django.contrib.auth.models import User
import uuid


# class User(models.Model):
#     # TODO: Gargi and monica
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     # Add more fields as needed

# class Cuisine(models.Model):
#     name = models.CharField(max_length=100)

#     # New fields
#     description = models.CharField(max_length = 128, blank=True, null=True)
#     ratings = models.DecimalField(max_digits = 2, decimal_places = 1)

#     def __str__(self):
#         return self.name

# class Restaurant(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     cuisines = models.ManyToManyField(Cuisine)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=20)
#     phone_number = models.CharField(max_length=20)
#     website = models.URLField(blank=True, null=True)

#     # New fields
#     is_open = models.BooleanField(default = True)


#     def __str__(self):
#         return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    favorite_food = models.CharField(max_length=100, blank=True)
    favorite_restaurant = models.CharField(max_length=100, blank=True)
    # additional fields for user settings will be updated as per requirements

    def __str__(self):
        return self.user.username

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     details = models.TextField()
#     ratings = models.FloatField(default=0)  # Assuming ratings will be a float number
#     comments = models.TextField(blank=True)
#     flag = models.CharField(max_length=10, choices=[('Veg', 'Veg'), ('Non Veg', 'Non Veg')])
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # ForeignKey relationship to Restaurant model

#     def __str__(self):
#         return self.name
# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
#     # check the dependency with restaurant
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     items = models.ManyToManyField(MenuItem)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order #{self.id} by {self.user.username} at {self.restaurant.name} on {self.order_date}"


# class Payments:
#     # TODO: Vinit
#     pass


class Comment(models.Model):
    # Short title of the comment
    title = models.CharField(max_length=100)
    # Detailed comment
    details = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add more fields as needed




class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)

    menus = models.ManyToManyField(MenuItem, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.order_id}"


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

    # reference of the restaurant the review was given to
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # rating given to the restaurant
    ratings = models.IntegerField(default=0, choices=RATINGS_RANGE)

    # comment associated with the review
    comment = models.TextField(blank=True, null=True, help_text='Add your comment')

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Review for {self.restaurant} by {self.user.username} ({self.ratings} stars)"

