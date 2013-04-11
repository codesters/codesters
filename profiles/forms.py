from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from profiles.models import UserProfile, Snippet

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('github', 'twitter', 'stackoverflow', 'facebook', 'website', 'gravatar_email', 'bio')

class SnippetCreateForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'content', 'show')

class SnippetUpdateForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'content', 'show')
