from django import forms
from app.models import Review
from .models import Customer, UserProfile


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ratings', 'comment']
        widgets = {
            'ratings': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
        }
        labels = {
            'ratings': 'Ratings',
            'comment': 'Comment',
        }


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', 'email', 'date_of_birth', 'contact_number']
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)



class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('bio', 'favorite_food', 'favorite_restaurant', 'profile_picture',)
