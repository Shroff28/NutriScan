from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render

from .models import User, UserProfile, Order, Restaurant, Cuisine, Menu, Payments, Review, Comment

