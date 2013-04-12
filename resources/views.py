from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse_lazy
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import SetHeadlineMixin

from django.contrib.auth.models import User
from resources.models import Resource, Topic, ResourceType
from profiles.models import SavedResource

from resources.forms import ResourceCreateForm, ResourceUpdateForm

def resource_home(request):
    topics = Topic.objects.filter(resource__title__isnull=False).distinct()
    recent_resources = Resource.objects.all().order_by('-created_at')[:5]
    popular_resources = Resource.objects.all().order_by('-rating_votes')[:5]
    ctx = {
            'topics': topics,
            'recent_resources': recent_resources,
            'popular_resources': popular_resources,
        }
    return render_to_response('resources/home.html', ctx, context_instance=RequestContext(request))

class ResourceSaveView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        resource = get_object_or_404(Resource, pk=pk)
        SavedResource.objects.get_or_create(user=self.request.user, resource=resource)
        return reverse_lazy('resource_detail', kwargs={'pk':pk})


class ResourceListView(SetHeadlineMixin, ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_queryset(self):
        slug = self.kwargs['slug']
        order = {'recent':'-created_at', 'popular':'-rating_votes'}
        order_to_get = 'recent'
        if 'o' in self.request.GET and order:
            order_to_get = self.request.GET['o']
        if slug=='all':
            resources = Resource.objects.all().order_by(order[order_to_get])
            self.headline = str(slug).capitalize() + ' Resources'
        else:
            resource_type = get_object_or_404(ResourceType, slug=slug)
            resources = Resource.objects.filter(resource_type=resource_type).order_by(order[order_to_get])
            self.headline = str(resource_type.name).capitalize() + ' Resources'
        return resources

    def get_context_data(self, **kwargs):
        context = super(ResourceListView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        return context


class ResourceTopicListView(SetHeadlineMixin, ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_queryset(self):
        slug = self.kwargs['slug']
        slug = self.kwargs['slug']
        order = {'recent':'-created_at', 'popular':'-rating_votes'}
        order_to_get = 'popular'
        if 'o' in self.request.GET and order:
            order_to_get = self.request.GET['o']
        topic = get_object_or_404(Topic, slug=slug)
        resources = topic.resource_set.all().order_by(order[order_to_get])
        self.headline = str(topic.name).capitalize() +' Resources'
        return resources

    def get_context_data(self, **kwargs):
        context = super(ResourceTopicListView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        return context


class ResourceDetailView(SetHeadlineMixin, DetailView):
    model = Resource
    context_object_name = 'resource'
    template_name = 'resources/resource_detail.html'

    def get_object(self):
        resource = super(ResourceDetailView, self).get_object()
        self.headline = str(resource.title) + ' (' + str(resource.resource_type) + ') | Resource'
        try:
            sr = SavedResource.objects.get(user=self.request.user, resource=resource)
            self.already_saved = True
        except SavedResource.DoesNotExist:
            self.already_saved = False
        return resource

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailView, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct()
        context['topics'] = topics
        context['already_saved'] = self.already_saved
        return context


class ResourceCreateView(LoginRequiredMixin, SetHeadlineMixin, CreateView):
    form_class = ResourceCreateForm
    template_name = 'resources/resource_create.html'
    headline = 'Add new Resource'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ResourceCreateView, self).form_valid(form)


class ResourceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SetHeadlineMixin, UpdateView):
    form_class = ResourceUpdateForm
    model = Resource
    template_name = 'resources/resource_update.html'
    headline = 'Edit Resource'
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
