from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView, RedirectView
from guardian.mixins import LoginRequiredMixin
from braces.views import SetHeadlineMixin
from django.contrib.auth.models import User

def user_redirect_view(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponseRedirect(reverse('user_detail', kwargs={'username': user.username,}))


class ExploreView(SetHeadlineMixin, TemplateView):
    template_name = 'coming_soon.html'
    headline = 'Explore - Coming Soon'


class TrackHomeView(SetHeadlineMixin, TemplateView):
    template_name = 'coming_soon.html'
    headline = 'Tracks - Coming Soon'


class HomeView(SetHeadlineMixin, TemplateView):
    template_name = 'index.html'
    headline = 'Welcome'


class AboutView(SetHeadlineMixin, TemplateView):
    template_name = 'about.html'
    headline = 'About Us'


class ContactView(SetHeadlineMixin, TemplateView):
    template_name = 'contact.html'
    headline = 'Contact Us'


class GuidelinesView(SetHeadlineMixin, TemplateView):
    template_name = 'guidelines.html'
    headline = 'Guidelines'
