from django.views.generic import DetailView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from profiles.models import Student

class StudentDetailView(DetailView):
    context_object_name = 'student'
    template_name = 'profiles/student_detail.html'
    model = Student
