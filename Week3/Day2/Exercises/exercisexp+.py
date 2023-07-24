# Ex 1: Family
# class Family:
#     def __init__(self, members, last_name):
#         self.members=members
#         self.last_name = last_name
        
#     def born(self,**child):
#         self.members.append(child)
#         print(f'Congrats for the birth of {child["name"]}')
#         print(self.members)
    
#     def is_18(self, name):
#         for i in members:
#             if i["name"] == name:
#                 if i["age"] > 18:
#                     return True
#                 else:
#                     return False
    
#     def family_presentation(self):
#         print(self.last_name)
#         for i in members:
#             print(i["name"])
        
       
        
# members = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# family1 = Family(members, 'Smith')
# print(family1.members)
# # family1.born(name='Bill',age=0,gender='Male',is_child=True)
# # print(family1.is_18('Bill'))
# # print(family1.family_presentation())



# Ex 2: The Incredibles Family
# class TheIncredibles(Family):
#     def __init__(self, members, last_name):
#         super().__init__(members, last_name)
    
#     def use_power(self,name,power):
#         for i in members:
#             if i["name"] == name:
#                 if i["age"] > 18:
#                     print(f'he/she has {power} powers')
#                 else:
#                     print('they are not over 18 years old')
    
#     def incredible_presentation(self,name,power):
#         super().family_presentation
#         for i in members:
#             if i["name"] == name:
#                 print(f'{name}: {power}')
#             else:
#                 print('No power')
    
#     def new_born(self):
#         super().born

# family2 = TheIncredibles(members, 'Starks')
# family2.incredible_presentation(members, 'Speed')
# family2.born(name='Baby Jack',age=0,gender='Male',is_child=True, power='Unknown Power')
# family2.incredible_presentation(members, 'Speed')

        
        