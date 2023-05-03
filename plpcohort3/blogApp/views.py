from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def about_us(request):
    return render(request, 'about.html',{})

posts = [
    {
        'author': 'Anna',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'August 10, 2020'
    },
    {
        'author': 'Jane',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'August 1, 2020'
    }
]
def article(request):
    return render(request, 'post.html', {
        "articles": posts,
    })