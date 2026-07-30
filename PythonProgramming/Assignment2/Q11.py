#11. Write a program that prompts the user to input a number and reverse its digits.

num = int(input("Enter a positive number to reverse it "))
while(1):
  num1 = num
  if(num1>0):
    result = 0
    while(num>0):
      rim = num%10
      result = result*10 + rim
      num//=10
    print(f"The reverse of the number {num1} is {result}.")
    break
  else:
    num = int(input("Please enter a positive number "))