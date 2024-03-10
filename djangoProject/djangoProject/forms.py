from django import forms

from djangoProject.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['restaurant', 'rating', 'comment']
        widgets = {

            'rating': forms.Select(),
            'comment': forms.Textarea(attrs={'rows': 5})
        }
        labels = {
            'restaurant': 'Restaurant Name',
            'rating': 'Ratings',
            'comment': 'Comment',
        }

