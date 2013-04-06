from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse


from django.views.generic import TemplateView, ListView, RedirectView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from walls.models import Snippet, Wall, Tag

def user_redirect_view(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponseRedirect(reverse('user_detail', kwargs={'pk': user.pk,}))

class ExploreView(ListView):
    template_name = 'explore.html'
    context_object_name = 'snippets'
    queryset = Snippet.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ExploreView, self).get_context_data(**kwargs)
        walls = Wall.objects.all()
        users = User.objects.filter(is_active=True).exclude(pk=-1)
        context['walls'] = walls
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
