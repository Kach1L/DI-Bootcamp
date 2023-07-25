import datetime
import random
from faker import Faker
# Ex 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return (f'{self.amount} {self.currency}')
    
    def __int__(self):
        return (self.amount)
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self,other):
        if self.currency != other.currency:
            print(f'TypeError: Cannot add between Currency type {type(self.currency)} and {type(other.currency)}')



# Ex 3
def randnum():
    num = int(input('Choose a number from between 1 and 100'))
    gen = random.randint(1,100)
    if num == random:
        print('Success')
    else:
        print(f'not the same number. the number: {gen}')

# randnum()



# Ex 4
def randstring():
    mylist = ["Apple", "Grape", "Cherry", "Peach", "Melon"]
    print(random.choice(mylist))
# I don't know how to download the string module.  
# randstring()




# Ex 5
def todaysdate():
    today = datetime.date.today()
    print(f'Todays date is {today}')

# todaysdate()

    

# Ex 6
def untiljan():
    d1 = datetime.datetime(2023,7,25,15,8)
    d2 = datetime.datetime(2024,1,1,0,0)
    delta = d2 - d1
    print(f'the 1st of January is in {delta}')

# untiljan()
   


# Ex 7
def minslived():
    d1 = datetime.date(2008,1,31)
    d2 = datetime.date(2023,7,25)
    delta = d2 - d1
    print(f'I have lived for {delta*60} mins')

minslived()



# Ex 8
fake = Faker() 
users = [
    {
		'name':'charles',
        'address':'charles@gmail.com','email':30
	},
	{
		'name':'carl',
        'address':'carl@gmail.com','email':30
	},
	{
		'name':'chloe',
        'address':'chloe@gmail.com','email':30
	}
]


def addfake(users):
    fakeperson = {}
    fakeperson['name'] = fake.name()
    fakeperson['address'] = fake.address()
    fakeperson['email'] = fake.email()
    
    users.append(fakeperson)
    return users

print(addfake(users))
        
        
    
    
    
    
    
    
    
    
    
    
    
    
