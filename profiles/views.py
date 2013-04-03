from django.views.generic import DetailView, RedirectView, TemplateView, ListView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from profiles.models import Student
from feeds.models import Feed

from django.core.urlresolvers import reverse

class StudentProfileView(DetailView):
    context_object_name = 'student'
    template_name = 'profiles/student_profile.html'
    model = Student


class MyTracksView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'

class MyProjectsView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'

class MyFeedsView(LoginRequiredMixin, ListView):
    template_name = 'profiles/user_feeds.html'
    context_object_name = 'feeds'

    def get_queryset(self):
        return Feed.objects.filter(created_by=self.request.user)

class MyBlogView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('blog_detail', kwargs={'username':user.username})

class MyProfileView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        pk = Student.objects.get(user=user).id
        return reverse('student_profile', kwargs={'pk':pk})
