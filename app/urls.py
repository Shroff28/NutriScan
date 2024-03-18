"""
URL configuration for Foodies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.urls import path

from .views import login, sign_up, home, ask_money
from .views import temp_review_view, user_settings, payment_successful, filter_temp

urlpatterns = [
    path('ratings/<int:restaurant_id>/', temp_review_view, name='ratings'),
    path('settings/', user_settings, name='Settings'),
    path('signup/', sign_up, name='sign_up'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('payment/', ask_money, name='payment'),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('temp_filter/', filter_temp, name='temp_filter'),
]
