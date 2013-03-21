from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import TemplateView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from blog.models import Blog, Entry, Tag

from django.views.generic import ListView, DetailView

class BlogHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'blog_home.html'


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'entry_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        u = User.objects.get(username=username)
        blog = Blog.objects.get(user=u)
        context['blog'] = blog
        return context


class EntryListView(ListView):
    context_object_name = 'entry_list'
    template_name = 'entry_list.html'

    def get_queryset(self):
        username = self.kwargs['username']
        u = User.objects.get(username=username)
        blog = Blog.objects.get(user=u)
        entries = blog.entry_set.all()
        return entries

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        u = User.objects.get(username=username)
        blog = Blog.objects.get(user=u)
        context['blog'] = blog
        return context
