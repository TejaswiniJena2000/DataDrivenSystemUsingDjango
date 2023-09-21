from django import forms
from django.contrib.auth.forms import UserChangeForm  # Import UserChangeForm
from django.contrib.auth.models import User  # Import User model
from .models import Profile

class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User  # Use the correct User model import
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )

class ProfileAdditionalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            # Add additional profile fields here
        )
