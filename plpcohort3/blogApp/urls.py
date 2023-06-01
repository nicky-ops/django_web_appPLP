from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about_us, name = 'about_us'),
    path('articles/', views.article, name = 'articles'),
    path('details/<int:pk>/', views.articles_details, name = 'details'),
    path('create/', views.article_create, name = 'create'),
    path('update/<int:pk>/', views.article_update, name = 'update'),
]