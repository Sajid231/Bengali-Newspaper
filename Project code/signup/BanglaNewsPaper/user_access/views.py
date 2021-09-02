from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user_access.forms import SignUpForm


# Sign Up Functionality
def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect('Index')

        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'register_form': form})