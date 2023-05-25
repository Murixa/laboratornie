import tkinter as tk

class Restaurant:
    def init(self, name):
        self.name = name

class IceCreamStand(Restaurant):
    def init(self, name, flavors, location, working_hours):
        super().init(name)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def check_flavor(self, flavor):
        return flavor in self.flavors

    def display_menu(self):
        print("Menu:")
        print("1. Ice Cream on a Stick")
        print("2. Soft Serve Ice Cream")
        # Добавьте свои методы для других типов мороженого

    def serve_ice_cream(self, choice):
        if choice == 1:
            self.serve_ice_cream_on_a_stick()
        elif choice == 2:
            self.serve_soft_serve_ice_cream()
        else:
            print("Invalid choice.")

    def serve_ice_cream_on_a_stick(self):
        print("Serving Ice Cream on a Stick.")

    def serve_soft_serve_ice_cream(self):
        print("Serving Soft Serve Ice Cream.")

# Создание экземпляра IceCreamStand
flavors = ['Vanilla', 'Chocolate', 'Strawberry']
location = '123 Main Street'
working_hours = '9 AM - 9 PM'
ice_cream_stand = IceCreamStand('My Ice Cream Stand', flavors, location, working_hours)

# Вызов метода для вывода списка сортов мороженого
ice_cream_stand.display_flavors()

# Добавление нового сорта мороженого
new_flavor = 'Mint Chocolate Chip'
ice_cream_stand.add_flavor(new_flavor)

# Удаление сорта мороженого
removed_flavor = 'Strawberry'
ice_cream_stand.remove_flavor(removed_flavor)

# Проверка наличия сорта мороженого
flavor_to_check = 'Chocolate'
if ice_cream_stand.check_flavor(flavor_to_check):
    print(f"{flavor_to_check} is available.")
else:
    print(f"{flavor_to_check} is not available.")

# Отображение меню и обслуживание мороженого на основе выбора
ice_cream_stand.display_menu()
choice = int(input("Enter your choice: "))
ice_cream_stand.serve_ice_cream(choice)