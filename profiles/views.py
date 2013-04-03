from django.views.generic import DetailView, RedirectView, TemplateView, ListView

from django.contrib.auth.models import User
from profiles.models import Student
from feeds.models import Feed

from django.core.urlresolvers import reverse

class StudentProfileView(DetailView):
    context_object_name = 'student'
    template_name = 'profiles/student_profile.html'
    model = Student


class MyTracksView(TemplateView):
    template_name = 'coming_soon.html'

class MyProjectsView(TemplateView):
    template_name = 'coming_soon.html'

class MyFeedsView(ListView):
    template_name = 'profiles/user_feeds.html'
    context_object_name = 'feeds'

    def get_queryset(self):
        return Feed.objects.filter(created_by=self.request.user)

class MyProfileView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        pk = Student.objects.get(user=user).id
        return reverse('student_profile', kwargs={'pk':pk})

