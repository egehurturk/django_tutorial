from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # @Overriding form_valid function
    def form_valid(self, form):
        form.instance.author = self.request.user  # That form you are trying to submit, take that instance and set the user to the current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # @Overriding form_valid function
    def form_valid(self, form):
        form.instance.author = self.request.user  # That form you are trying to submit, take that instance and set the user to the current user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: # The UpdateView has a method called get_object which returns the object
            '''If the user that access the /post/<int:pk>/update rout is the author of the post:'''
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: # The UpdateView has a method called get_object which returns the object
            '''If the user that access the /post/<int:pk>/update rout is the author of the post:'''
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


