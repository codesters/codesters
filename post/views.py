from django.views.generic import TemplateView, ListView, DetailView

from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from post.models import Post, Tag, PostType
from profiles.models import Student

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-posted_on')
    context_object_name = 'posts'
    template_name = 'post_list.html'


class PostPopularListView(ListView):
    queryset = Post.objects.all().order_by('-vote')
    context_object_name = 'posts'
    template_name = 'post_list.html'


class PostTypeListView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        post_type = PostType.objects.get(slug=slug)
        return Post.objects.filter(post_type=post_type)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'
