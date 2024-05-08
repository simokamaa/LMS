from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def system_config_index(request):
    return render(request, "system_config.html")
