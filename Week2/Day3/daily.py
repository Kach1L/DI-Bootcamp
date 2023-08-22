# Challenge 1
word = input("Enter a word: ")

index_dict = {}

for index, letter in enumerate(word):
    if letter in index_dict:
        index_dict[letter].append(index)
    else:
        index_dict[letter] = [index]

print(index_dict)




# Challenge 2
# Define the items and their prices
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

money = '$300'

# Get the amount of money in the wallet
wallet = int(money[1:])  # Convert wallet string to an integer

# Initialize a list to store affordable items
affordable_items = []

# Iterate through items and check affordability
for item, price in items_purchase.items():
    item_price = int(price[1:].replace(',', ''))  # Convert item price string to an integer
    if item_price <= wallet:
        affordable_items.append(item)

# Sort the affordable items alphabetically
affordable_items.sort()

# Print the result
if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
