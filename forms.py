from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    chess_score = forms.IntegerField(label='Chess Score')
    profile_picture = forms.ImageField(label='Profile Picture', required=False)
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 3}))
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'chess_score', 'profile_picture', 'bio', 'date_of_birth')




