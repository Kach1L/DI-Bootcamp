# Data Types
# 1
# c

# Lists and Loops
# 1
# nums = [1,2,3,4,5,6,7,8,9,10]
# squares = [x for x in nums if x % 2 = 0]
# print(squares)

# 2
# nums = range(0,10)
# div = [i for i in nums if i % 2 = 0 and i % 3 = 0]
# print(div)

# 3
# student_list = [
#     {
#     "name": "John", 
#     "age": 24
#     }, 
#     {
#     "name": "Anna", 
#     "age": 22
#     }, 
#     {
#     "name": "Mike", 
#     "age": 25
#     }
# ]

# for student in student_list:
#     print(student)

# Function Behavior with *args and **kwargs
# def combine_words(*args,**words):
    # print(combine_words(args[0] + args[1] + words["first"] + words["second"] + words["third"]))
    # print('Hello ' + 'world. ' + 'Python ' + 'is ' + 'great!')
# combine_words("Hello", " world.", second=" is", third=" great!", first="Python")


# Object-Oriented Programming (OOP)
# class Vehicle:
    # def __init__(self,type=str,brand=str,year=int):
    #     self.type = type
    #     self.brand = brand
    #     self.year = year
    
    # def __getattribute__(self):
    #     print(self.type, self.brand, self.year)

# Vehicle('venza','toyota',2020)

# OOP Inheritance and Decorators
# class Car:
#     def __init__(self,brand=str,model=str,mileage=int):
#         self.brand = brand
#         self.model = model
#         self.mileage = mileage
    
#     def __getattribute__(self):
#         print(self.brand, self.model, self.mileage)

# Car('toyota','venz',7)

# class ElectricCar(Car):
#     def __init__(self, brand=str, model=str, mileage=int, __battery_capacity=float):
#         self.__battery_capacity = __battery_capacity
        
#         @property(__battery_capacity)
#         def __getattribute__(self):
#             print(property)
#             if self.__battery_capacity >= 0:
#                 @__battery_capacity.setter(90)
            
                
#         print(self.brand, self.model, self.mileage, self.__battery_capacity)
                

# 3
# class BankAccount:
#     def __init__(self,brand=str,model=str,mileage=int,__balance=float,__account_holder=str):
#         self.brand = brand
#         self.model = model
#         self.mileage = mileage
#         self.__balance = __balance
#         self.__account_holder = __account_holder
    
#     def deposit(self):
#         amount = float(input('How much do u want to deposit?'))
#         self.__balance += amount
#         return 'Amount deposited successfully'
        
#     def withdraw(self):
#         amount = float(input('How much do u want to deposit?'))
        
#         if amount > self.__balance:
#             print('Insufficient Balance')
        
#         else:
#             self.__balance += amount
#             return 'Amount deposited successfully'
        
#     def view_balance(self):
#         return self.__balance
    
#     @classmethod
#     def trackacc(cls):
#         print(cls.__account_holder)
        
#     @staticmethod
#     def policytext():
#         print("Bank policy message")



# DATA SCIENCE        
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # 1 
# numpy_array = np.arange(1,10).reshape(3,3)
    
# # Print the numpy array
# print("Numpy Array:")
# print(numpy_array)
# print()

# # 2
# # Create the pandas DataFrame
# df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})

# # Replace non-numeric values in column "A" with the mean of numeric values
# numeric_values = pd.to_numeric(df['A'], errors='coerce')
# mean_numeric = numeric_values.mean()
# df['A'] = df['A'].apply(lambda x: mean_numeric if pd.to_numeric(x, errors='coerce') != x else x)

# # 3
# # Plot a histogram of the "A" column using matplotlib
# plt.hist(df['A'], bins=10, color='blue', edgecolor='black')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram of Column A')
# plt.show()

# # Plot "A" and "B" columns of df using matplotlib
# plt.plot(df['A'], label='Column A', marker='o')
# plt.plot(df['B'], label='Column B', marker='x')
# plt.xlabel('Index')
# plt.ylabel('Values')
# plt.title('Columns A and B')
# plt.legend()
# plt.show()



# Django and Django REST


