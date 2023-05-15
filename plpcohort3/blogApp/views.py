from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def about_us(request):
    return render(request, 'about.html',{})
def article(request):
    posts = Post.objects.all()
    context = {
        "articles": posts
    }
    return render(request, "posts.html", context)

def articles_details(request,pk):
    post = Post.objects.get(pk=pk)