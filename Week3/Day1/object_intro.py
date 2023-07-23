class Animal:
    
    def __init__(self, name): # init - initialization
        self.name = name # self - reference to the object
        

obj1 = Animal(name='Dog')

print(obj1.name)

obj2 = Animal(name='Zebra')

print(obj2.name)