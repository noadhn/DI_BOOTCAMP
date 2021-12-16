import json


class MenuManager:
    def __init__(self):
        with open('menu.json', "r") as menu:
            self.menu = json.load(menu)
        self.items = self.menu['items']

    def show_menu(self):
        print("\nMENU:")
        for item in self.items:
            print(f"{item['name']} : {item['price']} $")

    def add_item(self, name, price):
        if self.items[item][name] in self.items:
            return
        else:
            new_item = {"name": name, "price": price}
            self.items.append(new_item)
        with open('menu.json', 'w') as menu:
            json.dump(self.menu, menu, indent=4)

    def remove_item(self, name):
        items = [item for item in self.items if item["name"] != name]
        with open('menu.json', 'w') as menu:
            json.dump(self.menu, menu, indent=4)


menu_list = MenuManager()
menu_list.add_item("Milkshake", 2)
# menu_list.remove_item("ham")
menu_list.show_menu()
