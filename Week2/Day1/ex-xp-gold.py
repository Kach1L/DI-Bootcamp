# Ex 1
# print("Hello world\n"*4)
# print("I love python\n"*4)



# Ex 2
month = int(input("what is your month(in number)?"))

if month == 12 or month < 3 and month != 0:
    print("Winter")
elif month >= 3 and month <= 5 :
    print("Spring")
elif month >= 6 and month <= 8 :
    print("Summer")
elif month >= 9 and month <= 11 :
    print("Autumn/Fall")
else:
    print("Error..... Stupid fish brain. I'll even buy u a calender at this point.")