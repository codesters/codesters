from django import forms
from django.forms import ModelForm

from resources.models import Resource, Topic

class ResourceCreateForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('created_by', 'slug')

class ResourceUpdateForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('created_by','slug')

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ('slug',)

class TopicUpdateForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ('slug',)
