from django.urls import path

from .views import HomeListNewsView, NewsListByCategoryView, DetailNewsView, AddNewsView, EditNewsView, DeleteNewsView

urlpatterns = [
    path('', HomeListNewsView.as_view(), name='news_home'),
    path('category/<int:category_id>/', NewsListByCategoryView.as_view(), name='news_category'),
    path('news/<int:pk>/', DetailNewsView.as_view(), name='news_detail'),
    path('news/news_add/', AddNewsView.as_view(), name='news_add'),
    path('news/news_edit/<int:pk>/', EditNewsView.as_view(), name='news_edit'),
    path('news/news_delete/<int:pk>/', DeleteNewsView.as_view(), name='news_delete'),
]