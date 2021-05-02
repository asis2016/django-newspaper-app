from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Article


class ArticleListView(ListView):
    """ Article list view. """
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """ Create a new article. """
    model = Article
    template_name = 'create.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """ Update a single article. """
    model = Article
    template_name = 'update.html'
    fields = '__all__'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDetailView(DetailView):
    """ See a single article. """
    model = Article
    template_name = 'detail.html'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete a single article. """
    model = Article
    template_name = 'delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('articles')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
