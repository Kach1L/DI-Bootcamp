class Dog :
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    # used to print the information about the object
    # used when we call the print method
    def __str__(self) :
        return f"the dog {self.name} is a {self.type}"
    
    def show_dog(self) :
       print(self) #the same as calling the __str__ dunder method

    
my_dog = Dog("Rex", "Labrador", 4)
# without the str dunder method
# print(my_dog) # <__main__.Dog object at 0x000002239A2F40D0>
# with the __str__ dunder method
print(my_dog) #the dog Rex is a Labrador
# my_dog.show_dog()

# print(my_dog.__str__()) # 'the dog Rex is a Labrador'
# same as doing print(my_dog)

print(str(my_dog))
# converting the object to a string
print(str(my_dog).upper()) #THE DOG REX IS A LABRADOR