from django.http import HttpResponseRedirect, Http404
from django.views.generic import DetailView, RedirectView, TemplateView, ListView, UpdateView, CreateView
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import SetHeadlineMixin

from django.contrib.auth.models import User
from profiles.models import UserProfile, Snippet, SavedResource, TopicFollow, Project
from resources.models import Resource

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy

from profiles.forms import UserUpdateForm, UserProfileUpdateForm, SnippetCreateForm, SnippetUpdateForm, ProjectCreateForm, ProjectUpdateForm


def user_redirect_view(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponseRedirect(reverse('user_info', kwargs={'username': user.username}))


class UserInfoView(SetHeadlineMixin, DetailView):
    context_object_name = 'userinfo'
    template_name = 'profiles/user_detail.html'
    model = User

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        self.headline = str(user.username) + ' info'
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


class UserResourcesView(SetHeadlineMixin, ListView):
    context_object_name = 'resources'
    template_name = 'profiles/user_resources.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        self.headline = str(user.username) + ' shared Resources'
        return user.resource_set.all()

    def get_context_data(self,**kwargs):
        context = super(UserResourcesView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class UserProjectsView(SetHeadlineMixin, ListView):
    context_object_name = 'projects'
    template_name = 'profiles/user_projects.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        self.headline = str(user.username) + ' Projects'
        return user.project_set.all()

    def get_context_data(self,**kwargs):
        context = super(UserProjectsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class ProjectCreateView(LoginRequiredMixin, SetHeadlineMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'profiles/project_form.html'
    headline = 'Add New Project'

    def form_valid(self, form):
        user = get_object_or_404(User, username =self.request.user.username)
        form.instance.user = user
        return super(ProjectCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_projects', kwargs={'username':self.request.user.username})

    def get_context_data(self,**kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class ProjectUpdateView(LoginRequiredMixin, SetHeadlineMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'profiles/project_form.html'
    headline = 'Edit Project'

    def form_valid(self, form):
        user = get_object_or_404(User, username =self.request.user.username)
        form.instance.user = user
        return super(ProjectUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_projects', kwargs={'username':self.request.user.username})

    def get_context_data(self,**kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class UserSnippetsView(SetHeadlineMixin, ListView):
    context_object_name = 'snippets'
    template_name = 'profiles/user_snippets.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        self.headline = str(user.username) + ' Wall'
        return Snippet.objects.filter(user=user).filter(show=True)

    def get_context_data(self,**kwargs):
        context = super(UserSnippetsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context

#TODO first implement a view_resource permission in models then add a Permission required mixin here
class UserHiddenSnippetsView(SetHeadlineMixin, ListView):
    context_object_name = 'snippets'
    template_name = 'profiles/user_snippets.html'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Snippet.objects.filter(user=user).filter(show=False)

    def get_context_data(self,**kwargs):
        context = super(UserHiddenSnippetsView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context


class SnippetDetailView(SetHeadlineMixin, DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'profiles/snippet_detail.html'

    def get_object(self):
        snippet = get_object_or_404(Snippet, pk=self.kwargs['pk'])
        if snippet.show:
            self.headline = str(snippet.title) + ' | Wall'
            return snippet
        else:
            raise Http404


class SnippetCreateView(LoginRequiredMixin, SetHeadlineMixin, CreateView):
    model = Snippet
    form_class = SnippetCreateForm
    template_name = 'profiles/snippet_create.html'
    headline = 'Create New Snippet'

    def form_valid(self, form):
        user = get_object_or_404(User, username =self.request.user.username)
        form.instance.user = user
        return super(SnippetCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_snippets', kwargs={'username':self.request.user.username})


class SnippetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SetHeadlineMixin, UpdateView):
    model = Snippet
    form_class = SnippetUpdateForm
    template_name = 'profiles/snippet_update.html'
    permission_required = 'profiles.change_snippet'
    headline = 'Edit Snippet'
    return_403 = True

    def get_success_url(self):
        return reverse_lazy('user_snippets', kwargs={'username':self.request.user.username})


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SetHeadlineMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name = 'profiles/user_update.html'
    success_url = reverse_lazy('my_settings')
    permission_required = 'auth.change_user'
    headline = 'Change Account Settings'
    return_403 = True

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SetHeadlineMixin, UpdateView):
    form_class = UserProfileUpdateForm
    model = UserProfile
    template_name = 'profiles/userprofile_update.html'
    permission_required = 'profiles.change_userprofile'
    headline = 'Change Profile Settings'
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
