#1. Write a Python program using function that add two numbers.
def add_two_numbers(a,b):
  return a+b
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(f"{a} + {b} = {add_two_numbers(a,b)}")

'''
Enter the first number 1
Enter the second number 2
1 + 2 = 3

'''