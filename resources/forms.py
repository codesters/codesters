#from django import forms
from django.forms import ModelForm

from .models import Resource, Topic

class ResourceCreateForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('created_by', 'slug', 'help_text', 'show')

class ResourceUpdateForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('created_by', 'slug', 'help_text', 'show')

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ('slug',)

class TopicUpdateForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ('slug',)
