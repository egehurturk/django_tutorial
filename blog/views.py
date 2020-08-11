from django.shortcuts import render

# Create your views here.

# Dummy data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 28, 2018',
    }
]


def home(request):
    context = {
        'posts': posts, # this value will be accessible in 'blog/hone.hmtl' with {% for post in posts %}...
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})