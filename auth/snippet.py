# models.py
from django.db import models
from django.contrib.auth.models import Group

class MenuItem(models.Model):
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

class Role(models.Model):
    name = models.CharField(max_length=100)
    menu_items = models.ManyToManyField(MenuItem)

# views.py
from django.shortcuts import render
from .models import MenuItem

def dashboard(request):
    # Assuming you have a way to determine the user's role
    user_role = 'Student'  # Replace this with actual logic to get user's role

    # Fetch menu items based on user's role
    menu_items = MenuItem.objects.filter(role__name=user_role)

    return render(request, 'dashboard.html', {'menu_items': menu_items})

# # dashboard.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Dashboard</title>
# </head>
# <body>
#     <h1>Welcome to the Dashboard</h1>
#     <ul>
#         {% for menu_item in menu_items %}
#             <li><a href="{{ menu_item.url }}">{{ menu_item.label }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>
