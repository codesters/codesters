from django.views.generic import DetailView, RedirectView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from profiles.models import Student

from django.core.urlresolvers import reverse

class StudentDetailView(DetailView):
    context_object_name = 'student'
    template_name = 'profiles/student_detail.html'
    model = Student


class ProfileRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        pk = Student.objects.get(user=user).id
        return reverse('student_detail', kwargs={'pk':pk})

