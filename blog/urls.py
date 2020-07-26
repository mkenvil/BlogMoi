from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('index-page/', views.index, name='index-page'),
    path('blog-post/', views.blog_post, name='blog-post'),
    path('blog-list/', views.blog_list, name='blog-list'),
    path('about-page/', views.about, name='about-page'),
]