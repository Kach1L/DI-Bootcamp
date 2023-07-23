class Farm:
    def __init__(self, name, add_animal1, add_animal2, add_animal3, get_info):
        self.name = name
        self.add_animal1 = add_animal1
        self.add_animal2 = add_animal2
        self.add_animal3 = add_animal3
        self.get_info = get_info
        
    def name(self):
        print(f"{self.name}'s farm\n\n")

    def add_animal(self):
        print(f'{self.add_animal1} : 5')
        print(f'{self.add_animal2} : 2')
        print(f'{self.add_animal3} : 12\n\n')
    
    def get_info(self):
        print(f'\t{self.get_info}0')
        
name1 = Farm(' ','McDonald', ' ', ' ', ' '  ' ')
print(name1.name)

add_animal1 = Farm
('cow', ' ', ' ', ' ', ' ')
print(add_animal1.add_animal)
add_animal2 = Farm('sheep', ' ', ' ', ' ', ' ')
print(add_animal2.add_animal)
add_animal3 = Farm('goat', ' ', ' ', ' ', ' ')
print(add_animal3.add_animal)

get_info1 = Farm('E-I-E-I-', ' ', ' ', ' ', ' ')
print(get_info1.get_info)


#     def title(self):
#         print(f"{self.name}'s farm\n\n")
    
#     def cows(self, cow):
#         self.cow = cow
#         print({self.cow})
    
#     def sheeps(self, sheep):
#         self.sheep = sheep
#         print({self.sheep})
    
#     def goats(self, goat):
#         self.goat = goat
#         print({self.goat})
        
# name1 = Farm('McDonald')
# name1.title()
# cow1 = Farm('cow : 5')
# cow1.cows()
# sheep1 = Farm('sheep : 2')
# sheep1.sheeps()
# goat1 = Farm('goat : 12')
# goat1.goats()
