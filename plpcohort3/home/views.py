from django.shortcuts import render
from .models import Post
# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {
        "articles": posts
    }
    return render(request, "home.html", context)
def about_view(request):
    return render(request, "about.html")