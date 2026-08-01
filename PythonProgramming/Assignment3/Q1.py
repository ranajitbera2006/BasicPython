#1. Write a program that prompts the user to input a number and determine whether the number is palindrome or not.
num = int(input("Enter a number "))
num1 = num
result = 0
while num>0 :
  rim = num%10
  result = result*10 + rim
  num//=10
if(num1 == result):
  print(f"The number {num1} is palindrome.")
else:
  print(f"The number {num1} is not palindrome.")