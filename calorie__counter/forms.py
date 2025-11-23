from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Calorie


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "age",
            "gender",
            "weight",
            "height",
        ]
        labels = {
            "name": "Full Name",
            "age": "Your Age(Years)",
            "gender": "Select your gender",
            "weight": "Your weight(Kg)",
            "height": "Your height(cm)",
        }


class CalorieForm(forms.ModelForm):

    class Meta:
        model = Calorie
        fields = ["item_name", "calorie_consumed", "date"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}
