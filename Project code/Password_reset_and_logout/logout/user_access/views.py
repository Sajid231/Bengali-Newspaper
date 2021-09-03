from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Logout Functionality
@login_required
def LogoutView(request):
    logout(request)
    return redirect('Index')
