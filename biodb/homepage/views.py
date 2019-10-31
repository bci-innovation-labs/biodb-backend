"""
homepage/views.py
"""
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    user = request.user

    if user.is_authenticated:
        return redirect("/dashboard")

    return render(request, "homepage/index.html", {
        'user': user,
    })


def about(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "homepage/about.html", context)


def contact(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "homepage/contact.html", context)
