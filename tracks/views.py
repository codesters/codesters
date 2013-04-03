from django.views.generic import TemplateView, RedirectView

from django.core.urlresolvers import reverse

class TrackHomeView(TemplateView):
    template_name = 'coming_soon.html'

#class TrackHomeView(RedirectView):
#    def get_redirect_url(self):
#        return reverse('coming_soon')
