'''
1. Create a program that takes two numbers from the user and performs the following operations using the math module:
   (i) Calculate the square root of both numbers.
   (ii) Find the ceiling and floor values.
   (iii) Calculate power (first number raised to the second number).
   (iv) Find the absolute difference between them.
'''
import math as m
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(f"{a}^0.5 = {m.sqrt(a)}")
print(f"{b}^0.5 = {m.sqrt(b)}")
print(f"ceiling of {a} is {m.ceil(a)}")
print(f"ceiling of {b} is {m.ceil(b)}")
print(f"Floor of {a} is {m.floor(a)}")
print(f"Floor of {b} is {m.ceil(b)}")
print(f"{a}^{b} = {m.pow(a,b)}")
print(f"{a} ~ {b} = {m.fabs(a-b)}")

'''
Enter the first number 9
Enter the second number 4
9^0.5 = 3.0
4^0.5 = 2.0
ceiling of 9 is 9
ceiling of 4 is 4
Floor of 9 is 9
Floor of 4 is 4
9^4 = 6561.0
9 ~ 4 = 5.0
'''