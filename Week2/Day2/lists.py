# List Ex 1
# colors = ["blue", "red", "yellow"]
# first_color = color[0]
# print(first_color)

# elements = ["blue", "red", "yellow", ["apple", "pear"]]
# fruit_element = elements[3][1]

# fav_colors = ["blue", "red", "yellow"]
# last_element = fav_colors[-1] #same
# print(last_element)

# last_element_second = fav_colors[len(fav_colors)-1] #same
#             # fav_colors[3-1]
#             # fav_colors[2]
#             # yellow which is the laste element of the list
# print(last_element_second)

# names = ["John", "Tom", "Lea", "Lysa"]

# add to the end of the list



# List Ex 2
# all_colors = ["red", "blue", "yellow"]

# guest_answer = input("choose a color and position divided by a dash\n")
# # Example answer = "1-green"
# list_answer = guest_answer.split("-")
# # ["1", "green"]
# all.colors.insert(int(list_answer[0]), list_answer[1])

# print(all_colors)

# all_colors[1] = "pink"
# print(all_colors)



# animals = ["horse", "cat", "dog",]
# animals.pop() # delete the last element
# print(animals)
# animals.pop(0)
# print(animals)


# my_animals = ["horse", 'cat', "dog"]
# deleted_animal = my_animals.pop[1]
# print = (f"the animal deleted was a {deleted_animal}")
# # the animal deleted was a cat
# my_animals(10) # error no position 10
# my_animals.remove("hamster") #ValueError: list.remove(x): x not in list



# Class Ex
for num in range(0,15):
    if num % 2 == 0 :
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")