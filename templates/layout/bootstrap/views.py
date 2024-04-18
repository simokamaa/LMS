# views.py
from django.shortcuts import render
from .models import App

def dashboard(request):
    user_apps = request.user.apps.all()
    return render(request, 'dashboard.html', {'user_apps': user_apps})
