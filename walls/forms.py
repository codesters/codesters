from django import forms
from django.forms import ModelForm

from walls.models import Snippet

class SnippetCreateForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ('slug','wall', 'created_by')

class SnippetUpdateForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ('slug','wall', 'created_by')
