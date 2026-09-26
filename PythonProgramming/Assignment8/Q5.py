#5. Write a Python program that takes two numbers from the user and prints their greatest common divisor (GCD) using math.gcd() and calculates their least common multiple (LCM) using: LCM(a,b) = (a*b) / GCD(a,b)
import math as m
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(f"GCD{a,b} = {m.gcd(a,b)}")
print(f"LCM{a,b} = {(a*b)/m.gcd(a,b)}")

'''
Enter the first number 4
Enter the second number 6
GCD(4, 6) = 2
LCM(4, 6) = 12.0
'''