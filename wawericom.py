import json
from django.conf import settings 

menu_file_path =  settings.BASE_DIR / "templates" / "layout" / "partials" / "menu" / "vertical" / "json" / "vertical_menu.json"

from apps.Lms_App.models import MenuItem

with open('menu_data.json', 'r') as file:
    menu_data = json.load(file)


def create_menu_items(menu_items, parent=None):
    for item in menu_items:
        menu_item = MenuItem.objects.create(
            name=item['name'],
            icon=item['icon'],
            slug=item['slug'],
            badge_color=item.get('badge', [None, None])[0],
            badge_count=int(item.get('badge', [None, None])[1]) if item.get('badge') else None,
            url=item.get('url'),
            external=item.get('external', False),
            permission=item.get('permission'),
            target=item.get('target'),
            parent=parent
        )
        if 'submenu' in item:
            create_menu_items(item['submenu'], parent=menu_item)

create_menu_items(menu_data)
