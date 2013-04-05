from django import forms
from django.forms import ModelForm

from feeds.models import Feed, Tag

class FeedCreateForm(ModelForm):
    class Meta:
        model = Feed
        exclude = ('created_by',)

class FeedUpdateForm(ModelForm):
    class Meta:
        model = Feed
        exclude = ('created_by',)

class TagCreateForm(ModelForm):
    class Meta:
        model = Tag

class TagUpdateForm(ModelForm):
    class Meta:
        model = Tag
