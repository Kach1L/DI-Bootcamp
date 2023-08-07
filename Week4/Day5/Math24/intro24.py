# from game24 import GameScreen
from faker import Faker
import psycopg2

class Begin:
    def __init__(self): 
        self.name = None
        self.username = None
        self.password = None
        self.age = None
    
    def welcome(self):
        fake = Faker()
        return f"Welcome to my Math24 game➕➖✖️ ➗2️⃣ 4️⃣\n\nWe have a variety of players that include: {fake.name()}, {fake.name()}, {fake.name()}, and so many MORE.\n\nSo let's get you signed in👍"
    
    def signup(self):
        names = ['Arthur','Alex','Dmitri','Yossi','Lise','Vitaly','Danik','Vladlena']
        ex_password = '5char'
        
        self.name = input("What is your name?\t")
        if self.name != names[0] and self.name != names[1] and self.name != names[2] and self.name != names[3] and self.name != names[4] and self.name != names[5] and self.name != names[6] and self.name != names[7]:
            print(f'Wrong spelling try again:\n\n')
        else:
            print('Processing')
            
        self.username = input("Write your username:\t")
        
        self.password = input("Create a password:\t")
        if len(self.password) < len(ex_password):
            print(f'Password is too small\n{self.password}')
        else:
            print('Processing')
        
        self.age = int(input("How old are you?\t"))
        if self.age < 5:            
            print('Go outside, you are too little to play.')
        else:
            print('Processing, updating database with this info') 


    def pyinsert(self):
        connection = psycopg2.connect(
        database="Math24SignIn",
        user="postgres",
        password="Kachikwulu1",
        host="localhost",
        port="5432"
        )
        
        # Create a cursor
        cursor = connection.cursor()

        # Insert data
        insert_query = "INSERT INTO RegTable (name, user_name, password, age) VALUES (%s, %s, %s, %s)"
        data_to_insert = (self.name, self.username, self.password, self.age)
        cursor.execute(insert_query, data_to_insert)

        # Commit changes
        connection.commit()

        # Close cursor and connection
        cursor.close()
        connection.close()

p1 = Begin()
print(p1.welcome())
print(p1.signup())
print(p1.pyinsert())



