from django.db import models
from django import forms

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    badge_color = models.CharField(max_length=20, null=True, blank=True)
    badge_count = models.IntegerField(null=True, blank=True)
    external = models.BooleanField(default=False)
    target = models.CharField(max_length=20, null=True, blank=True)

class SubMenuItem(models.Model):
    parent_menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='submenu')
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    permission = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    url = models.CharField(max_length=100)

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class SubMenuItemForm(forms.ModelForm):
    class Meta:
        model = SubMenuItem
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


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
