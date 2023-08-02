from menu_item import MenuItem
from menu_manager import MenuManager

class MenuProgram:
    @staticmethod
    def show_user_menu():
        print("Menu Program")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("E - Exit")
        choice = input("Enter your choice: ").strip().upper()

        if choice == "V":
            item_name = input("Enter item name to view: ")
            item = MenuManager.get_by_name(item_name)
            if item:
                print(f"Item Name: {item.item_name}, Price: {item.item_price}")
            else:
                print("Item not found.")
        
        elif choice == "A":
            MenuProgram.add_item_to_menu()
        
        elif choice == "D":
            MenuProgram.remove_item_from_menu()
        
        elif choice == "U":
            MenuProgram.update_item_from_menu()
        
        elif choice == "S":
            MenuProgram.show_restaurant_menu()
        
        elif choice == "E":
            MenuProgram.show_restaurant_menu()
            print("Exiting the program.")
            exit()
        
        else:
            print("Invalid choice.")

    @staticmethod
    def add_item_to_menu():
        item_name = input("Enter item name: ")
        item_price = int(input("Enter item price: "))
        new_item = MenuItem(item_name, item_price)
        new_item.save()
        print("Item was added successfully.")

    @staticmethod
    def remove_item_from_menu():
        item_name = input("Enter item name to delete: ")
        item = MenuManager.get_by_name(item_name)
        if item:
            item.delete()
            print("Item was deleted successfully.")
        else:
            print("Item not found.")

    @staticmethod
    def update_item_from_menu():
        old_item_name = input("Enter item name to update: ")
        item = MenuManager.get_by_name(old_item_name)
        if item:
            new_item_name = input("Enter new item name: ")
            new_item_price = int(input("Enter new item price: "))
            item.update(new_name=new_item_name, new_price=new_item_price)
            print("Item was updated successfully.")
        else:
            print("Item not found.")

    @staticmethod
    def show_restaurant_menu():
        all_items = MenuManager.all_items()
        print("Restaurant Menu:")
        for item in all_items:
            print(f"Item Name: {item.item_name}, Price: {item.item_price}")

if __name__ == "__main__":
    while True:
        MenuProgram.show_user_menu()
