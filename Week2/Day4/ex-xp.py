# Ex 1
# def display_message(sentence):
#     return sentence

# print(display_message("We are learning python, javascript, html and css with frameworks"))



# Ex 2
# def favorite_book(title):
#     print(f"One of my favorite books is {title}.") 
#     return title

# (favorite_book("Wrinkle in Time"))



# Ex 3
# def describe_city(city, country = "Nigeria"):
#     print(f"{city} is in {country}")
#     return describe_city

# (describe_city("Abuja"))



# Ex 4
# import random
# def random_num(num1,num2):
#     if num1 == num2:
#         print('success, they are the same numbers.')
#     else:
#         print(f'failure. {num1} and {num2} were the numbers.')

# (random_num(7, random.randint(1,100)))



# Ex 5
# def make_shirt(size = 'large', text = 'I love Python', large_shirt = "Huge Hope", medium_shirt = "Medium Methods"):
#     print(f"The size of the shirt is {size} and the text is {text}. The other clothes texts are {large_shirt} and {medium_shirt}")
#     return make_shirt
# make_shirt("medium", "king",)



# Ex 6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magicians:list):
#     for name in magicians:
#         print(name)

# show_magicians(magician_names)

# new_list = []

# def make_great(magicians:list):
#     global magician_names
#     for i, name in enumerate(magician_names):
#         magician_names[i] = f'the Great {name}'
        
# make_great(magician_names)
# show_magicians(magician_names)



        


# Ex 7
# from random import randint

# def get_random_temp(season = int(input("choose a season"))):
#     if season==12 or 1 <= season <= 2:
#         print('winter')
#         temp = randint(-10.5, 16.5)
#     elif 3 <= season <= 6:
#         print('spring')
#         temp = randint(22.5, 26.5)
#     elif 7 <= season <= 9:
#         print('summer')
#         temp = randint(26.5, 36.5)
#     elif 10 <= season <= 11:
#         print('autumn')
#         temp = randint(16.5, 22.5)
#     return temp

# print(type(get_random_temp()))

# def main():
#     rand_temp = get_random_temp(input("choose a season"))
#     if rand_temp < 0:
#         print(f"Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 < rand_temp < 16:
#         print(f"Quite chilly! Don’t forget your coat")
#     elif 16 < rand_temp < 23:
#         print(f"Temp is between 16 and 23")
#     elif 23 < rand_temp < 32:
#         print(f"Temp is between 24 and 32")
#     elif 32 < rand_temp < 40:
#         print(f"Temp is between 32 and 40")

# main()



# Ex 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
failed = []
correct_ans = []
wrong_ans = []
def star_quiz():
    for i in data:
        print(i)
        ans = input('My Answer:')
        if ans != 'answer':
            wrong_ans.append[i]
            failed.append[i]
            print('wrong')
        elif ans == 'answer':
            correct_ans.append[i]
            print('correct')
        elif len(failed) >= 3:
            print('Kindly restart')
            return i 
        
star_quiz()

def informer():
    print(f'You got {correct_ans[-1]} correct')
    print(f'You got {wrong_ans[-1]} wrong')







