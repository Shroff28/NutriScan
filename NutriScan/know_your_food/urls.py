from django import views
from django.contrib import admin
from django.urls import path
from .views import login_view, signup, HomePageView,  upload_image, user_profile, meal_history, logout_view, update_profile

urlpatterns = [
    path('', login_view, name='loginPage'),
    path('signup/', signup, name='signup'),
    path('homePage/', HomePageView.as_view(), name="homePage"),
    path('imageUpload/', upload_image, name="imageUploadPage"),
    path('profile/', user_profile, name="profilePage"),
    path('meal-history/', meal_history, name="mealHisotry"),
    path('logout/', logout_view, name='logoutPage'),
    path('profile/', user_profile, name="profilePage"),
    path('update_profile/', update_profile, name="updateProfile")
    
    
]
