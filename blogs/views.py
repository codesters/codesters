from django.contrib.auth.models import User
from blogs.models import Blog, Entry, Tag

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, RedirectView

from blogs.forms import EntryCreateForm, EntryUpdateForm, BlogUpdateForm

class BlogHomeView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self):
        pk = User.objects.get(username='admin').pk
        return reverse('blog_detail', kwargs={'pk':pk})

#TODO Add permission
class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'blogs/blog_update.html'
    permission_required = 'blogs.change_blog'
    return_403 = True

    def get_context_data(self, **kwargs):
        context = super(BlogUpdateView, self).get_context_data(**kwargs)
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        context['blog'] = blog
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogUpdateView, self).form_valid(form)

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryCreateForm
    template_name = 'blogs/entry_create.html'

    def get_context_data(self, **kwargs):
        context = super(EntryCreateView, self).get_context_data(**kwargs)
        blog = Blog.objects.get(user=self.request.user)
        context['blog'] = blog
        return context

    def form_valid(self, form):
        blog = get_object_or_404(Blog, user=self.request.user)
        form.instance.blog = blog
        return super(EntryCreateView, self).form_valid(form)

class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'blog/entry_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        entry = get_object_or_404(Entry, pk=self.kwargs['pk'])
        context['blog'] = entry.blog
        return context

class EntryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Entry
    form_class = EntryUpdateForm
    template_name = 'blogs/entry_update.html'
    permission_required = 'blogs.change_entry'
    return_403 = True

    def get_context_data(self, **kwargs):
        context = super(EntryUpdateView, self).get_context_data(**kwargs)
        blog = Blog.objects.get(user=self.request.user)
        context['blog'] = blog
        return context

class EntryListView(ListView):
    context_object_name = 'entry_list'
    template_name = 'blog/entry_list.html'
    paginate_by = 12

    def get_queryset(self):
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        entries = blog.entry_set.all()
        return entries

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        context['blog'] = blog
        return context
