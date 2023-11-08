
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from main.forms import CommentForm
from main.models import Category, Service, Comment, Blog


class CategoryListView(ListView):
    """Описание views для модели Category"""
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'category'


class MedlistView(ListView):
    """Описание views для модели Service"""
    model = Service
    template_name = 'main/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(category_id=self.kwargs.get('pk'))
        queryset = queryset.filter(
            category_id=self.kwargs.get('pk')
        )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'{category_item.name}'
        return context_data


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'main/service_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ContactsListView(ListView):
    """Описание views для модели Contact"""
    model = Category
    template_name = 'main/contacts.html'


class CommentListView(ListView):
    """Описание views для модели Comment"""
    model = Comment
    template_name = 'main/comment_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super().form_valid(form)


class BLogListView(ListView):
    """Описание views для модели Blog"""
    model = Blog
    template_name = 'main/blog_list.html'
    context_object_name = 'blog'


class BLogDetailView(DetailView):
    model = Blog
    template_name = 'main/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
