from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm
from .utils import MyMixin

from .models import News, Category


class HomeListNewsView(ListView, MyMixin):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsListByCategoryView(ListView, MyMixin):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class DetailNewsView(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/news_detail.html'


class AddNewsView(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_add.html'
    login_url = '/admin/'


class EditNewsView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_edit.html'
    login_url = '/admin/'


class DeleteNewsView(LoginRequiredMixin, DeleteView):  # new
    model = News
    template_name = "news/news_delete.html"
    success_url = reverse_lazy("news_home")
