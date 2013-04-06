from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView

from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from resources.models import Resource, Topic, ResourceType

from resources.forms import ResourceCreateForm, ResourceUpdateForm

class ResourceHomeView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse_lazy('resource_recent_list')


class ResourceRecentListView(ListView):
    queryset = Resource.objects.all().order_by('-created_at')
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ResourceRecentListView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        return context


class ResourcePopularListView(ListView):
    queryset = Resource.objects.all().order_by('-vote')
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ResourcePopularListView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        return context


class ResourceTypeListView(ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_queryset(self):
        slug = self.kwargs['slug']
        resource_type = get_object_or_404(ResourceType, slug=slug)
        return Resource.objects.filter(resource_type=resource_type)

    def get_context_data(self, **kwargs):
        context = super(ResourceTypeListView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        return context


class ResourceTopicListView(ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_queryset(self):
        slug = self.kwargs['slug']
        topic = get_object_or_404(Topic, slug=slug)
        return topic.resource_set.all()

    def get_context_data(self, **kwargs):
        context = super(ResourceTopicListView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        return context


class ResourceRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        resource = get_object_or_404(Resource, pk=pk)
        resource.upvote(1)
        return resource.url

class ResourceDetailView(DetailView):
    model = Resource
    context_object_name = 'resource'
    template_name = 'resources/resource_detail.html'

    def get_object(self):
        resource = super(ResourceDetailView, self).get_object()
        resource.upvote(2)
        return resource


class ResourceCreateView(LoginRequiredMixin, CreateView):
    form_class = ResourceCreateForm
    template_name = 'resources/resource_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ResourceCreateView, self).form_valid(form)


class ResourceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ResourceUpdateForm
    model = Resource
    template_name = 'resources/resource_update.html'
    permission_required = 'resources.change_resource'
    return_403 = True

class TopicCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView): #mixin require an object, so make a get_object method
    model = Topic
    template_name = 'resources/topic_create.html'
    permission_required = 'resources.add_topic'
    render_403 = True

class TopicUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Topic
    template_name = 'resources/topic_update.html'
    permission_required = 'resources.change_topic'
    render_403 = True
