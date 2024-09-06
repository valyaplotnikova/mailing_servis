from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', )
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.add_blog'


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', )
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        return reverse('about', args=[self.kwargs.get('pk')])


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    permission_required = 'blog.delete_blog'
