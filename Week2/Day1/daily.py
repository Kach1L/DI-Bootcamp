# import random
# Ex 1 & 2
user_string = input("Write a string that is at least 10 characters long\n")

if len(user_string) < 10:
    print("string not long enough")
elif len(user_string) > 10:
    print("string too long")
else:
    print("perfect string")

print("First: ", user_string[0]) 
print("Last: ", user_string[-1])


# Ex 3
# hello_world_build = ["h", "he", "hel", "hell", "hello", 'hello w', 'hello wo', 'hello wor', "hello worl", 'hello world']
# for i in hello_world_build:
#     print(i)

#Ex 4
# intro = 'Helloworld'
# random.shuffle(intro)

# print(intro)




