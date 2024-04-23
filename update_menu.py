import templates.layout.partials.menu.vertical.json.vertical_menu.json as json
from apps.Lms_App.models import MenuItem

def update_menu_items(menu_items, parent=None):
    for item in menu_items:
        # Check if the menu item already exists in the database
        try:
            menu_item = MenuItem.objects.get(slug=item['slug'])
            # Update the existing menu item with data from the JSON file
            menu_item.name = item['name']
            menu_item.icon = item['icon']
            menu_item.badge_color = item.get('badge', [None, None])[0]
            menu_item.badge_count = int(item.get('badge', [None, None])[1]) if item.get('badge') else None
            menu_item.url = item.get('url')
            menu_item.external = item.get('external', False)
            menu_item.permission = item.get('permission')
            menu_item.target = item.get('target')
            menu_item.parent = parent
            menu_item.save()
        except MenuItem.DoesNotExist:
            # If the menu item does not exist, create a new one
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

        # If the menu item has submenus, recursively update them
        if 'submenu' in item:
            update_menu_items(item['submenu'], parent=menu_item)

# Load the updated JSON file
with open('menu_data.json', 'r') as file:
    updated_menu_data = json.load(file)

# Update the menu items
update_menu_items(updated_menu_data)
