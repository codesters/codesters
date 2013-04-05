from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from profiles.models import UserProfile

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('github', 'twitter', 'website', 'stackoverflow', 'coderwall', 'linkedin','bio')
