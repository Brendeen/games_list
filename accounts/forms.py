from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# linking our custom user model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age", "birthday")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age", "birthday")
