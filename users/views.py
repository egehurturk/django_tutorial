from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    """[register()]
    The register view handles the logic for registrating a user.

    Args:
        request ([HttpResponse]): [request that contains information about method.]

    Returns:
        [redirect]: [Redirection]
    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})
    



