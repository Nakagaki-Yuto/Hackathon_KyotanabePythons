from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserCreateForm(UserCreationForm):
    pass


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "mail", "university", "grade", "gender", "is_university"
        )

