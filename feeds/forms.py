from django import forms
from django.forms import ModelForm

from feeds.models import Feed

class FeedCreateForm(ModelForm):
    class Meta:
        model = Feed
        exclude = ('created_by',)

class FeedUpdateForm(ModelForm):
    class Meta:
        model = Feed
        exclude = ('created_by',)
