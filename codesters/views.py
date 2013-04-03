from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import TemplateView, ListView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from profiles.models import Student
from blogs.models import Entry, Blog, Tag

class ExploreView(ListView):
    template_name = 'explore.html'
    context_object_name = 'entries'
    queryset = Entry.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ExploreView, self).get_context_data(**kwargs)
        blogs = Blog.objects.all()
        users = User.objects.filter(is_active=True)
        context['blogs'] = blogs
        context['users'] = users
        return context

class SettingsView(TemplateView):
    template_name = 'profile.html'

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class GuidelinesView(TemplateView):
    template_name = 'guidelines.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
