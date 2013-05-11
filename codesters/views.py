from django.views.generic import TemplateView
from braces.views import SetHeadlineMixin


class ExploreView(SetHeadlineMixin, TemplateView):
    template_name = 'coming_soon.html'
    headline = 'Explore - Coming Soon'


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
