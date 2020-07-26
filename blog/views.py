from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'blog/home.html')


def index(request):
    return render(request, 'blog/index.html')


def blog_post(request):
    return render(request, 'blog/blog-post.html')


def blog_list(request):
    return render(request, 'blog/blog-list.html')


def about(request):
    return render(request, 'blog/about.html')
