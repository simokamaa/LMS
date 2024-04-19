# views.py
import json

from django.conf import settings
from django.http import HttpResponse

from .models import Menu, MenuItem

menu_file_path =  settings.BASE_DIR / "templates" / "layout" / "partials" / "menu" / "vertical" / "json" / "vertical_menu.json"


def parse_vertical_menu(request):
    # Assuming vertical_menu.json is located in a specific directory
    menu_file_path = './vertical_menu.json'

    # Open and read the JSON file
    with open(menu_file_path, 'r') as f:
        menu_data = json.load(f)

    # Parse the JSON data and save it to the database
    for menu_item_data in menu_data:
        # Create a Menu object
        menu = Menu.objects.create(name=menu_item_data['name'])

        # Create MenuItem objects for submenu items
        for submenu_item_data in menu_item_data.get('submenu', []):
            MenuItem.objects.create(
                name=submenu_item_data['name'],
                url=submenu_item_data['url'],
                menu=menu  # Associate the menu item with the parent menu
            )

    # Redirect or render a response as needed
    return HttpResponse("Menu structure parsed and saved to the database.")
