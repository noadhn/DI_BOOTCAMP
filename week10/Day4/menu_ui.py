import json
with open('menu.json', "r") as menu:
    menu = json.loads(menu.read())

shown_menu = json.dumps(menu, indent=2)

print("\nMENU:")
for item in menu['items']:
    print(f"{item['name']} : {item['price']} $")