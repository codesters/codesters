from django import forms
from django.forms import ModelForm

from blogs.models import Entry, Blog

class EntryCreateForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('slug','blog')

class EntryUpdateForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('slug','blog')

class BlogUpdateForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('user',)
