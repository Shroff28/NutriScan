from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Recipe, Nutritional_Info
from django.urls import reverse
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
from django.db.models import Q, F, Sum
from django.utils import timezone
from datetime import datetime, timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib import messages 


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == "POST":
        login_email = request.POST.get('email')
        login_password = request.POST.get('psw')
        user = authenticate(request, email=login_email,
                            password=login_password)
        if user:
            auth_login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            user = User.objects.get(email=user)
            request.session['user_id'] = user.id
            request.session['auth_token'] = token.key
            request.session.set_expiry(360)
            return redirect('homePage')
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    return render(request, 'html/login.html', {'user': request.user})


@api_view(['GET'])
def logout_view(request):
    logout(request)
    return redirect('loginPage')


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        confirm_password = request.POST.get('cpsw')
        if password == confirm_password:
            user = User.objects.create(
                fname=fname, lname=lname, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect(reverse('loginPage'))
        else:
            messages.error(
                request, 'Password and confirm password do not match.')

    return render(request, 'html/signup.html')


class HomePageView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            return render(request, 'html/homePage.html', {'user': user})


@login_required
@api_view(['GET', 'POST'])
def upload_image(request):
    predicted_label = None
    current_time = timezone.now().date()
    current_date = timezone.now().date()
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        image = Image.open(image_file)
        processor = AutoImageProcessor.from_pretrained(
            "./know_your_food/food")
        model = AutoModelForImageClassification.from_pretrained(
            "./know_your_food/food")
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        predicted_index = outputs.logits.argmax(dim=1).item()
        predicted_label = model.config.id2label[predicted_index]
        recipe_name = predicted_label
        user_id = request.session.get('user_id')
        user = get_object_or_404(User, id=user_id)
        existing_recipe = Nutritional_Info.objects.filter(
            Q(recipe_name__icontains=recipe_name)).first()
        if existing_recipe:
            existing_recipe_calorie = existing_recipe.calories
            print(Recipe.objects.filter(
                recipe_name=recipe_name,
                created_at__date=current_time).first())
            recipe_instance = Recipe.objects.filter(
                recipe_name=recipe_name,
                created_at__date=current_time).first()
            if recipe_instance:
                print("recipe_instance", recipe_instance)
                recipe_instance.calories = F(
                    'calories') + existing_recipe_calorie
                recipe_instance.save()
            else:
                print("create new")
                recipe_instance = Recipe.objects.create(
                    recipe_name=existing_recipe.recipe_name,
                    calories=existing_recipe.calories,
                    created_at=current_time,
                    user_id=user.id
                )
            return JsonResponse({"predicted_label": {"name": existing_recipe.recipe_name,
                                                     "serving": existing_recipe.serving,
                                                     "total_fat": existing_recipe.total_fat,
                                                     "saturated_fat": existing_recipe.saturated_fat,
                                                     "cholesterol": existing_recipe.cholesterol,
                                                     "sodium": existing_recipe.sodium,
                                                     "total_carbohydrates": existing_recipe.total_carbohydrates,
                                                     "dietary_fiber": existing_recipe.dietary_fiber,
                                                     "sugars": existing_recipe.sugars,
                                                     "proteins": existing_recipe.proteins,
                                                     "calories": existing_recipe.calories
                                                     }})
        # return render(request, 'html/imageUpload.html', {"predicted_label": predicted_label}
    return render(request, 'html/imageUpload.html')


@login_required
@api_view(['GET', 'POST'])
def user_profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = get_object_or_404(User, id=user_id)
        email = user.email
        first_name = user.fname
        last_name = user.lname
        print({'user': user, 'email': email,
              'first_name': first_name, 'last_name': last_name})
        return render(request, 'html/userProfile.html', {'user': user, 'email1': email, 'first_name': first_name, 'last_name': last_name})
    return render(request, 'html/userProfile.html')


@login_required
@api_view(['GET', 'POST'])
def meal_history(request):
    print("fsdvdfvdfv")
    seven_days_ago = datetime.now() - timedelta(days=7)

    top_recipes = Recipe.objects.filter(
        created_at__gte=seven_days_ago
    ).values('recipe_name', 'created_at').annotate(total_calories=Sum('calories')).order_by('recipe_name', 'created_at')
    top_recipes = list(top_recipes)
    for recipe in top_recipes:
        recipe['created_at'] = recipe['created_at'].isoformat()

    # Serialize top_recipes to JSON
    top_recipes_json = json.dumps(top_recipes, cls=DjangoJSONEncoder)
    return render(request, 'html/mealHistory.html', {'top_recipes_json': top_recipes_json, "top_recipes": top_recipes})
    # return render(request, 'html/mealHistory.html', {'top_recipes': json.dumps(list(top_recipes), cls=DjangoJSONEncoder)})

@login_required
@api_view(['GET', 'POST'])
def user_profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            # Get the updated profile data from the form
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            # Update the user's profile data
            user.email = email
            user.fname = first_name
            user.lname = last_name
            user.save()
            messages.success(request, 'Profile updated successfully!')
        # Fetch updated user data after saving changes
        user.refresh_from_db()
        return render(request, 'html/userProfile.html', {'user': user})
    return render(request, 'html/userProfile.html')

@login_required
@api_view(['POST'])
def update_profile(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            # Update the user's profile information with the data from the form
            user.fname = request.POST.get('fname')
            user.lname = request.POST.get('lname')
            user.email = request.POST.get('email')
            user.save()
            # Redirect to the user profile page after updating the profile
            return redirect('html:userProfile.html')
    # Handle other cases such as GET request or invalid data
    return redirect('html:userProfile.html')