"""
dashboard/views.py
"""

from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import render


def dashboard_page(request):
    user = request.user
    print("THE USER IS", user)

    if user.is_authenticated == False:
        return HttpResponse("Cannot view page - you must log in first!")

    context = {
        'user': user,
    }

    return render(request, "dashboard/dashboard.html", context)
