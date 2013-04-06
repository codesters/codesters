from django.views.generic import DetailView, RedirectView, TemplateView, ListView, UpdateView
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.models import User
from profiles.models import UserProfile
from resources.models import Resource
from walls.models import Wall

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy

from profiles.forms import UserUpdateForm, UserProfileUpdateForm, WallUpdateForm

class WallUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Wall
    form_class = WallUpdateForm
    template_name = 'profiles/wall_update.html'
    permission_required = 'walls.change_wall'
    return_403 = True

    def get_context_data(self, **kwargs):
        context = super(WallUpdateView, self).get_context_data(**kwargs)
        wall = get_object_or_404(Wall, pk=self.kwargs['pk'])
        context['wall'] = wall
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WallUpdateView, self).form_valid(form)


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


class UserResourcesView(ListView):
    context_object_name = 'resources'
    template_name = 'profiles/user_resources.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.resource_set.all()

    def get_context_data(self,**kwargs):
        context = super(UserResourcesView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['userinfo'] = user
        return context


class UserProjectsView(TemplateView):
    template_name = 'profiles/user_projects.html'

    def get_context_data(self,**kwargs):
        context = super(UserProjectsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['userinfo'] = user
        return context

class UserSnippetsView(ListView):
    context_object_name = 'snippets'
    template_name = 'profiles/user_snippets.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.wall.snippet_set.all()[:5]

    def get_context_data(self,**kwargs):
        context = super(UserSnippetsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['userinfo'] = user
        return context


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name = 'profiles/user_update.html'
    success_url = reverse_lazy('my_settings')
    permission_required = 'auth.change_user'
    return_403 = True


class UserProfileUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserProfileUpdateForm
    model = UserProfile
    template_name = 'profiles/userprofile_update.html'
    permission_required = 'profiles.change_userprofile'
    return_403 = True


class MySettingsView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('userprofile_update', kwargs={'pk': user.userprofile.pk})


class MyTracksView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'


class MyProjectsView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_projects', kwargs={'pk':user.pk})


class MyResourcesView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_resources', kwargs={'pk':user.pk})


class MyWallView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('wall_detail', kwargs={'pk':user.wall.pk})


class MyProfileView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_detail', kwargs={'pk':user.id})
