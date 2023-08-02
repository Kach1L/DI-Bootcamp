import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        connection = psycopg2.connect(database="menu_db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (item_name,))
        item_data = cursor.fetchone()
        connection.close()

        if item_data:
            return MenuItem(item_data[1], item_data[2])
        else:
            return None
        
item2 = MenuManager.get_by_name('Beef Stew')
    
@classmethod
def all_items(cls):
        connection = psycopg2.connect(database="menu_db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Menu_Items")
        all_items_data = cursor.fetchall()
        connection.close()

        all_items = []
        for item_data in all_items_data:
            all_items.append(MenuItem(item_data[1], item_data[2]))

        return all_items
items = MenuManager.all()