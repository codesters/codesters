from django import forms
from django.forms import ModelForm

from blogs.models import Entry

class EntryCreateForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('slug','blog')

class EntryUpdateForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('slug','blog')
