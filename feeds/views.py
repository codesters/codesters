from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from feeds.models import Feed, Tag, FeedType
from profiles.models import Student

from feeds.forms import FeedCreateForm, FeedUpdateForm

class FeedListView(ListView):
    queryset = Feed.objects.all().order_by('-created_on')
    context_object_name = 'feeds'
    template_name = 'feeds/feed_list.html'

    def get_context_data(self, **kwargs):
        context = super(FeedListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedPopularListView(ListView):
    queryset = Feed.objects.all().order_by('-vote')
    context_object_name = 'feeds'
    template_name = 'feeds/feed_list.html'

    def get_context_data(self, **kwargs):
        context = super(FeedPopularListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedTypeListView(ListView):
    context_object_name = 'feeds'
    template_name = 'feeds/feed_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        feed_type = FeedType.objects.get(slug=slug)
        return Feed.objects.filter(feed_type=feed_type)

    def get_context_data(self, **kwargs):
        context = super(FeedTypeListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedTagListView(ListView):
    context_object_name = 'feeds'
    template_name = 'feeds/feed_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=slug)
        return tag.feed_set.all()

    def get_context_data(self, **kwargs):
        context = super(FeedTagListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedDetailView(DetailView):
    model = Feed
    context_object_name = 'feed'
    template_name = 'feeds/feed_detail.html'

    def get_object(self):
        feed = super(FeedDetailView, self).get_object()
        feed.vote += 2
        feed.save()
        return feed


class FeedCreateView(LoginRequiredMixin, CreateView):
    form_class = FeedCreateForm
    template_name = 'feeds/feed_create.html'

    def form_valid(self, form):
        student = Student.objects.get(user=self.request.user)
        form.instance.created_by = student
        return super(FeedCreateView, self).form_valid(form)


class FeedUpdateView(LoginRequiredMixin, UpdateView):
    form_class = FeedUpdateForm
    model = Feed
    template_name = 'feeds/feed_create.html'
