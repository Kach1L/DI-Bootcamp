# Ex 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# combination = dict(zip(keys, values))
# print(combination)



# Ex 2
# Ticket pricing function
# def calculate_ticket_price(age):
#     if age < 3:
#         return 0
#     elif 3 <= age <= 12:
#         return 10
#     else:
#         return 15

# # Using the provided family dictionary
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# total_cost = 0

# print("Cost for each family member:")

# for name, age in family.items():
#     cost = calculate_ticket_price(age)
#     total_cost += cost
#     print(f"{name.capitalize()}: ${cost:.2f}")

# print(f"\nTotal cost for the family: ${total_cost:.2f}")

# # Initialize an empty family dictionary
# family = {}

# # Get input from the user
# num_family_members = int(input("Enter the number of family members: "))

# for i in range(num_family_members):
#     name = input(f"Enter the name of family member {i + 1}: ")
#     age = int(input(f"Enter the age of {name}: "))
#     family[name] = age

# total_cost = 0

# print("\nCost for each family member:")

# for name, age in family.items():
#     cost = calculate_ticket_price(age)
#     total_cost += cost
#     print(f"{name.capitalize()}: ${cost:.2f}")

# print(f"\nTotal cost for the family: ${total_cost:.2f}")



# Ex 3 
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": ["blue"],
#         "Spain": ["red"],
#         "US": ["pink", "green"]
#     }
# }
# print(brand)
# brand.pop('creation_date')
# print(brand)
# print("international_competitors")

# more_on_zara = {}
# more_on_zara["creation_date"] = "1975"
# more_on_zara["number_stores"] = "10 000"

# def Merge(brand, more_on_zara):
#     return(more_on_zara.update(brand))
# print(more_on_zara["number_stores"])

# # Change the number of stores to 2
# brand["number_stores"] = 2

# # Print a sentence about Zara's clients
# print("Zara's clients are men, women, children, and home buyers.")

# # Add country_creation key
# brand["country_creation"] = "Spain"

# # Add "Desigual" to international_competitors
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")

# # Delete the creation_date
# del brand["creation_date"]

# # Print the last international competitor
# print("Last international competitor:", brand["international_competitors"][-1])

# # Print major clothes colors in the US
# print("Major clothes colors in the US:", brand["major_color"]["US"])

# # Print the amount of key-value pairs
# print("Number of key-value pairs:", len(brand))

# # Print the keys of the dictionary
# print("Keys:", list(brand.keys()))

# # Create another dictionary
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }

# # Use method to add more_on_zara to brand
# brand.update(more_on_zara)

# # Print the value of the key number_stores
# print("Number of stores:", brand["number_stores"])



# Ex 4
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# # Recreate result 1 using a loop
# disney_users_A = {}
# for i, character in enumerate(users):
#     disney_users_A[character] = i
# print("Result 1:", disney_users_A)

# # Recreate result 2 using a loop
# disney_users_B = {}
# for i, character in enumerate(users):
#     disney_users_B[i] = character
# print("Result 2:", disney_users_B)

# # Recreate result 3 using a method and sorting
# disney_users_C = {}
# for i, character in enumerate(sorted(users)):
#     disney_users_C[character] = i
# print("Result 3:", disney_users_C)

# # Recreate result 1 for characters with names containing "i"
# disney_users_I = {}
# for i, character in enumerate(users):
#     if "i" in character.lower():
#         disney_users_I[character] = i
# print("Result 1 for 'i' characters:", disney_users_I)

# # Recreate result 1 for characters with names starting with "m" or "p"
# disney_users_MP = {}
# for i, character in enumerate(users):
#     if character.startswith("M") or character.startswith("P"):
#         disney_users_MP[character] = i
# print("Result 1 for 'M' or 'P' characters:", disney_users_MP)







