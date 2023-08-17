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
        
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# np.arange(1,10).reshape(3,3)
    


