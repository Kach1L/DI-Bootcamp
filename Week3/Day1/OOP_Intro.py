# Class - the basis of OOP (Object oriented...)
# Class is what alows creating objects

class Animal:

    # class variable 
    population = 100000

    @classmethod # class method = class function 
    def voice(cls): # cls = reference to the class (Animal)
        print("AAAA")


# Creating instances of class
dog = Animal()

print(type(dog))
print(dog.population)
dog.voice()

print(Animal.population)
Animal.voice()



class Computer:

    @classmethod
    def computeA(cls):
        pass
    @classmethod
    def computeB(cls):
        pass

class Printer:

    @classmethod
    def printZ(cls):
        pass