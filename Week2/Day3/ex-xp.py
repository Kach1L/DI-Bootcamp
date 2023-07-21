# Ex 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# combination = dict(zip(keys, values))
# print(combination)



# Ex 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# amount = [0, 0, 0, 0]

# for fam in family:
#     if family[fam] > 12:
#         print('the ticket is $15.')
#         amount += 15
#     elif 3 < family[fam] < 12:
#         print('the ticket is $10.')
#         amount += 10
#     else:
#         print('the ticket is free.')

# print(f"Rick's cost is ${amount[0]}. Beth's cost is ${amount[1]}. Morty's cost is ${amount[2]}. Summer's cost is ${amount[3]}.")

# Bonus
# family = {}
# name = "name"
# age = "age"
# i = 0

# while i < 20:
#     user_answer = print(input('What is your name and age? Ex morty, 15'))
#     user_info = user_answer.split(', ')
#     print(user_info)
#     family[user_info[0]] = user_info[1]
#     print(family)

#     if user_answer == 'q':
#         print('Family check complete')
#         break



# Ex 3 
brand = {
"name" : "Zara",
"creation_date" : "1975",
"creator_name" : "Amancio Ortega Gaona",
"type_of_clothes" : "men, women, children, home",
"international_competitors" : "Gap, H&M, Benetton, Desigual",
"number_stores" : "2",
"major_color" : {"France" : "blue", "Spain" : "red", "US" : ["pink", "green"]},
"country_creation" : "Spain",
}
print(brand)
brand.pop('creation_date')
print(brand)
print("international_competitors")

more_on_zara = {}
more_on_zara["creation_date"] = "1975"
more_on_zara["number_stores"] = "10 000"

def Merge(brand, more_on_zara):
    return(more_on_zara.update(brand))
print(more_on_zara["number_stores"])



# Ex 4
# disney_users_A = {}
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# numbers = []

# for num in range(0, 5):
#     numbers.append(num)

# disney_users_A = dict(zip(users, numbers))

# disney_users_B = {}
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# numbers = []

# for num in range(0, 5):
#     numbers.append(num)

# disney_users_B = dict(zip(numbers, users))

# Exercise 3 : Disney Characters

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# indexes = [i for i in range(len(users))]

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# outputA = dict(zip(sorted(users), indexes))
# print(outputA)

# disney_users_A2 = {}
# users = ["Mickey","Minnie","Ariel","Pluto"]
# numbers = []

# for num in range(0, 4):
#     numbers.append(num)

# disney_users_A2 = dict(zip(users, numbers))







