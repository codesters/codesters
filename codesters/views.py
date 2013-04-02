from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import TemplateView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

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
