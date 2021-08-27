from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user_access.forms import LoginForm


# Login functionality
def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("Index")

            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = LoginForm()
        return render(request=request, template_name="login.html", context={"login_form": form})
