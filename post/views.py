from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from post.models import Post, Tag, PostType
from profiles.models import Student

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-posted_on')
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class PostPopularListView(ListView):
    queryset = Post.objects.all().order_by('-vote')
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostPopularListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class PostTypeListView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        post_type = PostType.objects.get(slug=slug)
        return Post.objects.filter(post_type=post_type)

    def get_context_data(self, **kwargs):
        context = super(PostTypeListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class PostTagListView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=slug)
        return tag.post_set.all()

    def get_context_data(self, **kwargs):
        context = super(PostTagListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_create.html'
