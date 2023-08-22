# Ex 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
        
# cat1 = Cat('Bob', 10)
# cat2 = Cat('Bat', 11)
# cat3 = Cat('Bill', 9)

# # windows - Alt for multiple lines
# # mac - option

# def oldest_cat(cat_list: list[Cat]) -> Cat | None:
#     if len(cat_list) == 0:
#         return None
    
#     oldest_cat = cat_list[0]
    
#     for cat in cat_list:
#         if cat.age > oldest_cat.age:
#             old_age = cat.age
#             oldest_cat = cat
    
#     return oldest_cat
# oldest = oldest_cat([cat1, cat2, cat3])
# print(f'The oldest cat is {oldest.name}, and is {oldest.age} years old.')




# Ex 2
# class Dog:
#     def __init__(self, name, height):
#          self.name = name
#          self.height = height
         
#     def bark(self):
#         print(f'{self.name} goes woof!')
    
#     def jump(self):
#         print(f'{self.name} jumps {self.height*2}cm high!.')
    
# dog1 = Dog('Jack', 30)
# print(dog1.name)
# print(dog1.height)
# dog2 = Dog('Star', 25)
# dog2.bark()
# dog3 = Dog('Bart', 40)
# dog3.jump()




# Ex 3
# class Song:
#     def __init__(self, lyrics=list):
#         self.lyrics = lyrics
        
#     def sing_me_a_song(self):
#         lyrics= (f'{self.lyrics[0]}\n{self.lyrics[1]}\n{self.lyrics[2]}')
#         print(lyrics)
#         return lyrics
            
# lyrics1 = Song(["There's a lady who's sure","all that glitters is gold","and she's buying a stairway to heaven"])
# lyrics1.sing_me_a_song()



# Ex 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo!")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} sold from the zoo!")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].capitalize()
            if len(first_letter) not in sorted_animals:
                sorted_animals[len(first_letter)] = []
            sorted_animals[len(first_letter)].append(animal)
        
        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Animals grouped by first letter:")
        for length, animals in sorted_animals.items():
            print(f"{length}: {animals}")


# Create an object called ramat_gan_safari
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Add animals
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Gorilla")
ramat_gan_safari.add_animal("Giraffe")  # This won't be added since it's a duplicate

# Get animals
ramat_gan_safari.get_animals()

# Sell an animal
ramat_gan_safari.sell_animal("Lion")

# Sort and get groups
groups = ramat_gan_safari.sort_animals()
print(groups)

# Print animals in each group
ramat_gan_safari.get_groups()
