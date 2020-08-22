from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)



def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post # Tell the listview what model to query in order to create the list
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # This will order our posts from newest to oldest.


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    # @Overriding form_valid function
    def form_valid(self, form):
        form.instance.author = self.request.user # That form you are trying to submit, take that instance and set the user to the current user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})









# DAKKA 31 SANIYE 40 TA KALDIM HA!

# By default, CBV looks for a certain template
# We can make a CBV look a template by adding the template_name field.
# ListView's pass the variable as the `object_list` variable
# We can either change that variable in templates, or
# we can use the `context_object_use`.
# When we look at an individual post, this will be detailview
# DetailView will have `object` variable pass to html files.
# In home.html, when we have a variable in URl, we can use the `{% url 'post-detail' post.id %} syntax
# In CreateView, we need to provide the field that we want to be in that form.
# In CreateView, it shares the template with the UpdateView
# They actually expect this to be `<model>_<form>`
# With these changes made, we now actually can't submit a form, because it does not know the user.
# We can accomplish by overriding the `form_save()` method.
# Then, it throws an error saying that it does not redirect to any page.
# We can create a `get_absoulte_url` method in the `models.py` to every model.
#    We should use the return `reverse` function!.
#    Redirect will actually redirect you to the page
#    Reverse will return the full url to that rout as a string.