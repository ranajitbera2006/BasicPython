#1. Write a program that prompts the user to input three integers and outputs the largest.

num1 = int(input("Please enter the first number "))
num2 = int(input("Please enter the second number "))
num3 = int(input("Please enter the third number "))
if(num1>=num2 and num1>=num3):
  print(f"The first number {num1} is greatest.")
elif(num2>=num3):
  print(f"The second number {num2} is greatest.")
else:
  print(f"The third number {num3} is greatest.")