# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         print(f'{self.name} is just walking around')

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# cat1 = Bengal('Beatrice', 6)
# cat2 = Chartreux('Ben', 9)
# cat3 = Siamese('Beth', 5)
# all_cats = [cat1,cat2,cat3]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

 
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
    
#     def bark(self):
#         print(f'{self.name} is barking')
    
#     def run_speed(self):
#         return self.weight/self.age*10
    
#     def fight(self, other_dog):
#         if self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
#             print(f'{other_dog.name} won the fight')
#         else:
#             print(f'{self.name} won the fight')

# dog1 = Dog('Pat',8,20)
# dog2 = Dog('Tara',5,13)
# dog3 = Dog('Rufus',10,26)

# dog1.bark()
# dog1.run_speed()
# dog1.fight(dog3)

# dog2.bark()
# dog2.run_speed()
# dog2.fight(dog1)

# dog3.bark()
# dog3.run_speed()
# dog3.fight(dog1)
        

