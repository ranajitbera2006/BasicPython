#12. Write a program that prompts the user to input two integers and outputs the larger.

num1 = int(input("Please enter the first number "))
num2 = int(input("Please enter the second number "))
if(num1>num2):
  print(f"The first number {num1} is greatest.")
else:
  print(f"The second number {num2} is greatest.")