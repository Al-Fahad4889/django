from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm  # Assuming SignUpForm is defined in forms.py in your app
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')  # Redirect to the homepage (make sure you have a home view defined)
    else:
        form = SignUpForm()
    
    # Adjusted path to reflect the correct template location
    return render(request, 'signup.html', {'form': form})

# user/views.py
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('auth.view_sensitive_data', raise_exception=True)
def sensitive_info_view(request):
    return HttpResponse("This is sensitive information only accessible to authorized users.")


@permission_required('auth.view_sensitive_data', raise_exception=True)
def sensitive_info_view(request):
    return HttpResponse("This is sensitive information only accessible to authorized users.")
