# Ex 1
# my_fav_numbers = {7, 14, 3, 8}
# my_fav_numbers.insert(1, 2)
# my_fav_numbers.append(10)
# my_fav_numbers.pop(-1)

# friend_fav_numbers = {9, 15, 4, 11}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) 
# print(our_fav_numbers)


# Ex 2
# Given a tuple which value is integers, is it possible to add more integers to the tuple? No. Tuples are unchangeable.



# Ex 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(-1)
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)



# Ex 4
# num_list = []
# for num in range(1, 6):
#     num_list.append(num) 
#     dec = num + 0.5
#     num_list.append(dec)
# print(num_list)



# Ex 5
# for num in range(1,21):
#     if num % 2 == 0:
#         print(num)



# Ex 6
# my_name = "Kachi"
# name = input("What is your name?\n")
# while name != my_name:
#     print("What is your name?\n")
# else:
#     print("We have the same name\n")



# Ex 7
# fav_fruits = input("What are your favorite fruits? Please separate the fruits with a single space, eg. apple mango cherry")
# fav_fruits.split(" ")

# fav_fruit = input("What is your favorite fruit?")
# if fav_fruit == fav_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")


# Ex 8
# toppings = []
# price_per_topping = 2.5

# while True:
#     topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
#     if topping.lower() == 'quit':
#         break
    
#     toppings.append(topping)
#     print(f"Adding {topping} to your pizza.")

# total_price = 10 + len(toppings) * price_per_topping

# print("\nToppings on your pizza:")
# for topping in toppings:
#     print(topping)

# print(f"\nTotal price: ${total_price:.2f}")



# Ex 9
# Calculate ticket price based on age
# def calculate_ticket_price(age):
#     if age < 3:
#         return 0
#     elif 3 <= age <= 12:
#         return 10
#     else:
#         return 15

# # Ask for family members' ages
# num_family_members = int(input("Enter the number of family members: "))
# total_cost = 0

# for i in range(num_family_members):
#     age = int(input(f"Enter the age of family member {i + 1}: "))
#     ticket_price = calculate_ticket_price(age)
#     total_cost += ticket_price

# print(f"Total cost for the family's tickets: ${total_cost:.2f}")


# # Calculate ticket price based on age
# def calculate_ticket_price(age):
#     if age < 3:
#         return 0
#     elif 3 <= age <= 12:
#         return 10
#     else:
#         return 15

# # Ask for family members' ages
# num_family_members = int(input("Enter the number of family members: "))
# total_cost = 0

# for i in range(num_family_members):
#     age = int(input(f"Enter the age of family member {i + 1}: "))
#     ticket_price = calculate_ticket_price(age)
#     total_cost += ticket_price

# print(f"Total cost for the family's tickets: ${total_cost:.2f}")


# Ex 10
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# finished_sandwiches = []

# # Remove all occurrences of "Pastrami sandwich" from sandwich_orders
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")

# # Prepare the orders and move them to finished_sandwiches
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(current_sandwich)
#     print(f"I made your {current_sandwich.lower()}")

# print("\nList of sandwiches that were made:")
# for sandwich in finished_sandwiches:
#     print(sandwich)












