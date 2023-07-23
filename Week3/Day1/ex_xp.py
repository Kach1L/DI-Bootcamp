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
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         lyrics= (f'{self.lyrics}')
#         print(lyrics)
            
# lyrics1 = Song("There's a lady who's sure\nall that glitters is gold\nand she's buying a stairway to heaven")
# lyrics1.sing_me_a_song()



# Ex 4
# class Zoo:
#     def __init__(self, zoo_name, animals):
#         self.zoo_name = zoo_name
#         self.animals = animals
#     def add_animal(self, new_animal):
#         animals = ['Baboon', "Bear", 'Cat', 'Cougar', 'Eel', 'Emu', "Ape"]
        
#         animals_sorted = sorted(animals)

#         print(animals_sorted)

#         animals_groups = {}

#         animal_check = animals_sorted[0]
#         group = 1

#         animals_groups[group] = [animal_check] 
#         for animal in animals_sorted[1:]:
#             if animal_check[0] == animal[0]: 
#                 animals_groups[group].append(animal)
#         else:
#             group += 1 # 3
#         animals_groups[group] = [animal]
#         animal_check = animal # Cat
    
#         print(animals_groups)
    
#     def get_animals(self):
#         animals = ['Baboon', "Bear", 'Cat', 'Cougar', 'Eel', 'Emu', "Ape"]
#         animals_sorted = sorted(animals)
#         print(animals_sorted)
        
#     def sell_animals(self, animal_sold):
#         animals = ['Baboon', "Bear", 'Cat', 'Cougar', 'Eel', 'Emu', "Ape"]
#         for ani in animals:
#             if ani == animal_sold:
#                 animals -= ani
            

#     def sort_animals(self):
#         animals = ['Baboon', "Bear", 'Cat', 'Cougar', 'Eel', 'Emu', "Ape"]

#         animals_sorted = sorted(animals)

#         print(animals_sorted)

#         animals_groups = {}


#     def get_groups(self):
#         animals = ['Baboon', "Bear", 'Cat', 'Cougar', 'Eel', 'Emu', "Ape"]
#         for ani in animals:
#             print(ani)
            
#     ramat_gam_safari = print('Which animal should we add to the zoo --> Baboon')
#     add_animal.add_animal('Baboon')



            
    








