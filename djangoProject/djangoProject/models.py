from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    #TODO: Gargi and monica
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add more fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    favorite_food = models.CharField(max_length=100, blank=True)
    favorite_restaurant = models.CharField(max_length=100, blank=True)
    # additional fields for user settings will be updated as per requirements
    
    def __str__(self):
        return self.user.username

class Restaurant:
    #TODO: Astha

class Menu:
    # TODO: Dhrumil

class Order:
    # TODO: Jaydeep

class Payments:
    #TODO: Vinit


