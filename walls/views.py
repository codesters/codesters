from django.contrib.auth.models import User
from walls.models import Wall, Snippet, Tag

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404
from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, RedirectView

from walls.forms import SnippetCreateForm, SnippetUpdateForm

class WallHomeView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self):
        pk = User.objects.get(username='admin').pk
        return reverse('wall_detail', kwargs={'pk':pk})


class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    form_class = SnippetCreateForm
    template_name = 'walls/snippet_create.html'

    def get_context_data(self, **kwargs):
        context = super(SnippetCreateView, self).get_context_data(**kwargs)
        wall = Wall.objects.get(user=self.request.user)
        context['wall'] = wall
        return context

    def form_valid(self, form):
        wall = get_object_or_404(Wall, user=self.request.user)
        form.instance.wall = wall
        return super(SnippetCreateView, self).form_valid(form)

class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'wall/snippet_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SnippetDetailView, self).get_context_data(**kwargs)
        snippet = get_object_or_404(Snippet, pk=self.kwargs['pk'])
        context['wall'] = snippet.wall
        return context

class SnippetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Snippet
    form_class = SnippetUpdateForm
    template_name = 'walls/snippet_update.html'
    permission_required = 'walls.change_snippet'
    return_403 = True

    def get_context_data(self, **kwargs):
        context = super(SnippetUpdateView, self).get_context_data(**kwargs)
        wall = Wall.objects.get(user=self.request.user)
        context['wall'] = wall
        return context

class SnippetListView(ListView):
    context_object_name = 'snippet_list'
    template_name = 'wall/snippet_list.html'
    paginate_by = 12

    def get_queryset(self):
        wall = get_object_or_404(Wall, pk=self.kwargs['pk'])
        entries = wall.snippet_set.all()
        return entries

    def get_context_data(self, **kwargs):
        context = super(SnippetListView, self).get_context_data(**kwargs)
        wall = get_object_or_404(Wall, pk=self.kwargs['pk'])
        context['wall'] = wall
        return context
