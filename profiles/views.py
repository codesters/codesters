from django.views.generic import DetailView, RedirectView, TemplateView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from profiles.models import UserProfile
from feeds.models import Feed

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


class UserDetailView(DetailView):
    context_object_name = 'userinfo'
    template_name = 'profiles/user_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        userprofile = get_object_or_404(UserProfile, user=user) #redundancy check for user may exist but his profile not
        context['userprofile'] = userprofile
        return context


class MyTracksView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'

class MyProjectsView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'

class MyFeedsView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('feed_user_list', kwargs={'pk':user.pk})

class MyBlogView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('blog_detail', kwargs={'pk':user.blog.pk})

class MyProfileView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_detail', kwargs={'pk':user.id})
