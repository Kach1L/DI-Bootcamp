class Dog :
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    # used to print the information about the object
    # used when we call the print method
    def __str__(self) :
        return f"the dog {self.name} is a {self.type}"
    
    # used to print the information about the object
    # used for the developer in the shell
    def __repr__(self):
        return f"{self.name} - {self.type} - {self.age}"
    

    # def __add__(self, other_dog) :
    #     return self.age + other_dog.age

    # create a puppy from the combination of 2 dogs
    def __add__(self, other_dog) :
        user_choice = input("what is the name of the puppy \n")
        puppy_type = self.type[:6]+other_dog.type[6:]
        return Dog(user_choice,puppy_type, 0)

    def __gt__(self, other_dog):
        if isinstance(other_dog, Dog) :
            if self.age > other_dog.age:
                return self
            else :
                return other_dog
        else :
            print("not an instance")
    
    
my_dog = Dog("Rex", "Labrador", 4)
my_second_dog = Dog("Lola", "Chihuahua", 2)
print(my_dog + my_second_dog) 
# the dog Lola is a Labradhua

new_puppy = my_dog + my_second_dog
print(new_puppy)

# >>> my_dog > my_second_dog #call gt dunder method
# Rex - Labrador - 4 #call the repr dunder method

# in the shell
# my_dog # Rex - Labrador - 4  --> call the __repr__ dunder method
# print(my_dog) # the dog Rex is a Labrador --> call the __str__ dunder method