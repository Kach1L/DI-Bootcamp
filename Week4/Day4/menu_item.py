import psycopg2

class MenuItem:
    def __init__(self,item_name,item_price=0):
        self.item_name = item_name
        self.item_price = item_price
    
    def save(self):
        connection = psycopg2.connect(database="menu_db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                       (self.item_name, self.item_price))
        connection.commit()
        connection.close()

    def delete(self):
        connection = psycopg2.connect(database="menu_db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.item_name,))
        connection.commit()
        connection.close()

    def update(self, new_name=None, new_price=None):
        connection = psycopg2.connect(database="menu_db")
        cursor = connection.cursor()
        update_query = "UPDATE Menu_Items SET "
        update_values = []

        if new_name:
            update_query += "item_name = %s, "
            update_values.append(new_name)
        if new_price is not None:
            update_query += "item_price = %s, "
            update_values.append(new_price)

        # Remove the trailing comma and space from the query if there are updates
        if update_values:
            update_query = update_query[:-2]

        item = MenuItem('Burger', 35)
        item.save()
        update_query += " WHERE item_name = %s"
        update_values.append(self.item_name)

        cursor.execute(update_query, tuple(update_values))
        connection.commit()
        connection.close()

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)