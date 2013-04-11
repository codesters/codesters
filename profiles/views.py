from django.http import HttpResponseRedirect
from django.views.generic import DetailView, RedirectView, TemplateView, ListView, UpdateView, CreateView
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.models import User
from profiles.models import UserProfile, Snippet, SavedResource, TopicFollow
from resources.models import Resource

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy

from profiles.forms import UserUpdateForm, UserProfileUpdateForm, SnippetCreateForm, SnippetUpdateForm


def user_redirect_view(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponseRedirect(reverse('user_info', kwargs={'username': user.username}))


class UserInfoView(DetailView):
    context_object_name = 'userinfo'
    template_name = 'profiles/user_detail.html'
    model = User

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user

    def get_context_data(self, **kwargs):
        context = super(UserInfoView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        userprofile = get_object_or_404(UserProfile, user=user) #redundancy check for user may exist but his profile not
        saved_resources = SavedResource.objects.filter(user=user)
        topics_follow = TopicFollow.objects.filter(user=user)
        context['userprofile'] = userprofile
        context['saved_resources'] = saved_resources
        context['topics_follow'] = topics_follow
        return context


class UserResourcesView(ListView):
    context_object_name = 'resources'
    template_name = 'profiles/user_resources.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.resource_set.all()

    def get_context_data(self,**kwargs):
        context = super(UserResourcesView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class UserProjectsView(TemplateView):
    template_name = 'profiles/user_projects.html'

    def get_context_data(self,**kwargs):
        context = super(UserProjectsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context

class UserSnippetsView(ListView):
    context_object_name = 'snippets'
    template_name = 'profiles/user_snippets.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.snippet_set.all()

    def get_context_data(self,**kwargs):
        context = super(UserSnippetsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'profiles/snippet_detail.html'


class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    form_class = SnippetCreateForm
    template_name = 'profiles/snippet_create.html'

    def form_valid(self, form):
        user = get_object_or_404(User, username =self.request.user.username)
        form.instance.user = user
        return super(SnippetCreateView, self).form_valid(form)


class SnippetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Snippet
    form_class = SnippetUpdateForm
    template_name = 'profiles/snippet_update.html'
    permission_required = 'profiles.change_snippet'
    return_403 = True


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name = 'profiles/user_update.html'
    success_url = reverse_lazy('my_settings')
    permission_required = 'auth.change_user'
    return_403 = True

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserProfileUpdateForm
    model = UserProfile
    template_name = 'profiles/userprofile_update.html'
    permission_required = 'profiles.change_userprofile'
    return_403 = True

    def get_object(self):
        return self.request.user.userprofile


class MyResourcesView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_resources', kwargs={'username':user.username})



class MyProfileView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_detail', kwargs={'username':user.username})
