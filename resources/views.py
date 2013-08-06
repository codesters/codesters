from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.utils.datastructures import SortedDict
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import SetHeadlineMixin
from djangoratings.views import AddRatingView

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from .models import Resource, Topic, ResourceType, FeaturedResource
from profiles.models import SavedResource, TopicFollow

from .forms import ResourceCreateForm, ResourceUpdateForm, TopicCreateForm, TopicUpdateForm

def resource_home(request):
    topics = Topic.objects.filter(resource__title__isnull=False).distinct().order_by('name')

    #Check various session values for user details and show appropriate info
    #if request.session.get('no_name', False):
    #    messages.info(request, 'Please fill in your profile details by going to your account settings.')
    #    request.session['no_name'] = False

    if request.session.get('no_topic', False):
        messages.warning(request, 'It seems you are not following any topic. Follow topics by clicking on it below and get personalized recommendations')
        request.session['no_topic'] = False

    ctx = {
            'topics': topics,
        }
    return render_to_response('resources/resource_home.html', ctx, context_instance=RequestContext(request))

def rate_resource(request, object_id, score):
    model = 'resource'
    app_label = 'resources'
    field_name ='rating'
    try:
        content_type = ContentType.objects.get(model=model, app_label=app_label)
    except ContentType.DoesNotExist:
        raise Http404('Invalid `model` or `app_label`.')
    params = {
            'content_type_id': content_type.id,
            'object_id': object_id,
            'field_name': field_name,
            'score': score,
        }
    response = AddRatingView()(request, **params)
    if response.status_code == 200:
        if response.content == 'Vote recorded.':
            messages.success(request, 'Thanks, Your Vote is recorded')
    else:
        messages.error(request, 'Sorry, Something went wrong')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class ResourceSaveView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        resource = get_object_or_404(Resource, pk=pk)
        SavedResource.objects.get_or_create(user=self.request.user, resource=resource)
        if self.request.META['HTTP_REFERER']:
            return self.request.META['HTTP_REFERER']
        else:
            return reverse_lazy('resource_detail', kwargs={'pk':pk})


class ResourceFeatureView(LoginRequiredMixin, RedirectView):
    permanent = False
    permission_required = 'resources.change_featuredresource'
    return_403 = True

    def get_redirect_url(self, pk, slug):
        resource = get_object_or_404(Resource, pk=pk)
        topic = get_object_or_404(Topic, slug=slug)
        resource.make_featured(topic=topic)
        if self.request.META['HTTP_REFERER']:
            return self.request.META['HTTP_REFERER']
        else:
            return reverse_lazy('resource_detail', kwargs={'pk':pk})


class SidebarMixin(object):
    def get_context_data(self, **kwargs):
        context = super(SidebarMixin, self).get_context_data(**kwargs)
        topics = Topic.objects.filter(resource__title__isnull=False).distinct().order_by('name')
        context['topics'] = topics
        return context


class ResourceAllListView(SetHeadlineMixin, SidebarMixin, ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_queryset(self):
        level_to_get = None
        if 'level' in self.request.GET:
            level_to_get = self.request.GET['level']
        resources = Resource.objects.all()
        if level_to_get:
            resources = resources.filter(level=level_to_get)
        self.headline = 'All Resources'
        return resources


class TopicFollowView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, slug):
        topic = get_object_or_404(Topic, slug=slug)
        try:
            tf = TopicFollow.objects.get(user=self.request.user, topic=topic)
            tf.delete()
            messages.success(self.request, 'You have stopped following this topic.')
        except TopicFollow.DoesNotExist:
            TopicFollow.objects.create(user=self.request.user, topic=topic)
            messages.success(self.request, 'You are now following this topic.')
        return reverse_lazy('resource_topic_home', kwargs={'slug':slug})

def topic_home(request, slug):
    current_topic = get_object_or_404(Topic, slug=slug)
    headline = """Learn """ + unicode(current_topic.name).capitalize() + """ - from the best tutorials and online courses"""
    topics = Topic.objects.filter(resource__title__isnull=False).distinct().order_by('name')

    ctx = {
        'current_topic': current_topic,
        'headline': headline,
        'topics': topics
    }

    resourcetypes = []
    res_types = ResourceType.objects.all().order_by('name')
    for res_type in res_types:
        try:
            result = FeaturedResource.objects.get(topic=current_topic, resource_type=res_type)
            resourcetypes.append((result.resource_type.slug, result.resource))
        except FeaturedResource.DoesNotExist:
            result = current_topic.resource_set.filter(resource_type=res_type).order_by('-rating_votes')
            if len(result) > 0:
                resourcetypes.append((result[0].resource_type.slug, result[0]))
    ctx['resourcetypes'] = SortedDict(resourcetypes)

    return render_to_response('resources/topic_home.html', ctx, context_instance=RequestContext(request))


class ResourceTopicListView(SetHeadlineMixin, SidebarMixin, ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    paginate_by = 12

    def get_queryset(self):
        level_to_get = None
        res_type = None
        slug = self.kwargs['slug']
        try:
            res_type = self.kwargs['res_type']
        except KeyError:
            pass
        if 'level' in self.request.GET:
            level_to_get = self.request.GET['level']
        topic = get_object_or_404(Topic, slug=slug)
        resources = topic.resource_set.all()
        self.headline = 'All ' + unicode(topic.name).capitalize() +' Resources'
        if res_type:
            res_type = get_object_or_404(ResourceType, slug=res_type)
            resources = resources.filter(resource_type=res_type)
            self.headline = unicode(topic.name).capitalize() +' Resources' + ' (' + unicode(res_type.name) + 's)'
        if level_to_get and level_to_get != 'all':
            resources = resources.filter(level=level_to_get)
        return resources

    def get_context_data(self, **kwargs):
        context = super(ResourceTopicListView, self).get_context_data(**kwargs)
        topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
        context['current_topic'] = topic
        return context


class ResourceDetailView(SetHeadlineMixin, SidebarMixin, DetailView):
    model = Resource
    context_object_name = 'resource'
    template_name = 'resources/resource_detail.html'

    def get_object(self):
        resource = super(ResourceDetailView, self).get_object()
        self.headline = unicode(resource.title) + """ (""" + unicode(resource.resource_type) + """) | Resource"""
        return resource

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailView, self).get_context_data(**kwargs)
        return context


class ResourceCreateView(LoginRequiredMixin, SetHeadlineMixin, SidebarMixin, CreateView):
    form_class = ResourceCreateForm
    model = Resource
    headline = 'Add new Resource'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ResourceCreateView, self).form_valid(form)


class ResourceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SetHeadlineMixin, SidebarMixin, UpdateView):
    form_class = ResourceUpdateForm
    model = Resource
    headline = 'Edit Resource'
    permission_required = 'resources.change_resource'
    return_403 = True


class TopicCreateView(SetHeadlineMixin, SidebarMixin, CreateView):
    form_class = TopicCreateForm
    template_name = 'resources/topic_form.html'
    permission_required = 'resources.add_topic'
    headline = 'Create New Topic'


class TopicUpdateView(PermissionRequiredMixin, SetHeadlineMixin, SidebarMixin, UpdateView):
    form_class = TopicUpdateForm
    model = Topic
    template_name = 'resources/topic_form.html'
    permission_required = 'resources.change_topic'
    render_403 = True
    return_403 = True
    headline = 'Edit Topic'
