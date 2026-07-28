#7. Write a program that prompts the user to enter number in two variables and swap the contents of the variables.

num1 = int(input("Please enter the value of num1 "))
num2 = int(input("Please enter the value of num2 "))
temp = num1
num1 = num2
num2 = temp
print(f"num1 = {num1}\nnum2 = {num2}")