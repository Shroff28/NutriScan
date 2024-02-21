from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    #TODO: Gargi and monica
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add more fields as needed

class Restaurant:
    #TODO: Astha

class Menu:
    # TODO: Dhrumil

class Order:
    # TODO: Jaydeep

class Payments:
    #TODO: Vinit


