# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import json
from .models import App

@login_required
def initial_app_creation(request):
    if not App.objects.exists():
        # Only execute if no apps exist
        if request.user.is_superuser:
            # Load menu structure from JSON
            with open('vertical_menu.json') as menu_file:
                menu_data = json.load(menu_file)

            # Create app based on menu structure
            # Assuming the menu_data is a list of dictionaries containing app information
            for app_data in menu_data:
                app = App.objects.create(
                    name=app_data['name'],
                    icon=app_data.get('icon', ''),
                    slug=app_data['slug']
                )
                # Assign group permissions to the app based on the 'group' field in the menu data
                group_name = app_data.get('group')
                if group_name:
                    group, _ = Group.objects.get_or_create(name=group_name)
                    app.group.add(group)
            return redirect('sidebar')
    return redirect('home')  # Redirect to home page if apps already exist or user is not superuser

@login_required
def sidebar(request):
    user_groups = request.user.groups.all()
    user_apps = App.objects.filter(group__in=user_groups)
    return render(request, 'sidebar.html', {'user_apps': user_apps})


from django.db import models
from django.core.exceptions import ValidationError

class App(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

class Page(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='pages')
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    target = models.CharField(max_length=20, null=True, blank=True)

class AppLogic:
    @classmethod
    def create_apps_from_menu(cls, menu_data):
        created_apps = []
        for item in menu_data:
            if 'menu_header' not in item:
                app = cls.create_app_from_item(item)
                if app:
                    created_apps.append(app)
        return created_apps

    @classmethod
    def create_app_from_item(cls, item):
        try:
            app = App.objects.create(
                name=item['name'],
                icon=item['icon'],
                slug=item['slug']
            )
            if 'submenu' in item:
                cls.create_pages_for_app(app, item['submenu'])
            return app
        except KeyError as e:
            raise ValidationError(f"Required key {e} is missing in the menu item.")

    @classmethod
    def create_pages_for_app(cls, app, submenu_data):
        for subitem in submenu_data:
            if 'url' in subitem and 'name' in subitem:
                Page.objects.create(
                    app=app,
                    url=subitem['url'],
                    name=subitem['name'],
                    slug=subitem['slug'],
                    target=subitem.get('target')
                )

# Usage Example:
menu_data = [  # Assume this is your menu/submenu data
    {
        "name": "Dashboards",
        "icon": "menu-icon tf-icons ti ti-smart-home",
        "slug": "dashboard",
        "submenu": [
            {
                "url": "index",
                "name": "Analytics",
                "slug": "dashboard-analytics"
            },
            {
                "url": "dashboard-student",
                "name": "Students",
                "slug": "dashboard-student"
            },
            # Other submenu items...
        ]
    },
    {
        "name": "eCommerce",
        "icon": "menu-icon tf-icons ti ti-shopping-cart",
        "slug": "app-ecommerce",
        "submenu": [
            {
                "url": "app-ecommerce-dashboard",
                "name": "Dashboard",
                "slug": "app-ecommerce-dashboard"
            },
            # Other submenu items...
        ]
    },
    # Other menu items...
]

created_apps = AppLogic.create_apps_from_menu(menu_data)
print("Created apps:", created_apps)
