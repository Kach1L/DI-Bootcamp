# friend_age = 37

# if friend_age > 30:
#     print("you are an adult")
# elif 25 <= friend_age <= 29:
#     print("You are almost an adult")
# elif 20 <= friend_age <= 24:
#     print("You are not a child")
# else :
#     print("You are a child")

# print("end")


# Exercise 1
# name = 'John Doe'
# if len(name) > 20:
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = 'long'
# elif len(name) > 15:
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = 'semi long'
# elif len(name) > 10:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = 'semi long'
# elif 7 < len(name) < 11:
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = 'semi short'
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = 'short'



# Exercise 2
number_people = int(input("how many guests"))

if number_people > 200:
    print("the wedding will cost $20000")
elif 100 < number_people <= 200 :
    print("the wedding will cost $15000")

elif 50 < number_people <= 100 :
    print("the wedding will cost $10000")    

elif 0 < number_people <= 50 :
    print("the wedding will cost $4000")    

