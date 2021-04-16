from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # class meta gives nested namespace for config and keeps config in one place
    # and this class says that model that will be affected is model and
    # and the what fields are present and in what order
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# model form allows us to create a form that allows us work with a specific database model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
