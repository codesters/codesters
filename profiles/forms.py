from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import UserProfile, Project

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('github', 'twitter', 'stackoverflow', 'facebook', 'website', 'gravatar_email', 'bio')

class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'url', 'source_url', 'description')


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'url', 'source_url', 'description')
