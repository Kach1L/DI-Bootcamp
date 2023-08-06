from faker import Faker
# import psycopg2

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
    
        # connection = psycopg2.connect(
        #     database="Math24SignIn",
        #     user="postgres",
        #     password="Kachikwulu1",
        #     host="localhost",
        #     port="5432"
        # )
        

p1 = Begin()
print(p1.welcome())
print(p1.signup())



# self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.password = password
#         self.nationality = nationality
#         self.age = age


# ,first_name=input,last_name=input,user_name=input,password=input,nationality=input,age=int(input)