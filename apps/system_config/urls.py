from django.urls import path 
from . views import system_config_index

urlpatterns = [
    path('system_config/', system_config_index, name="system_config_index"),
]
