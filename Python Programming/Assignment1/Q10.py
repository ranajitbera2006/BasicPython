#10. Write a program that prompts the user to input a number and display if the number is even or odd.

num = int(input("Please enter a number to check is it even or odd "))
if(num%2==0):
  print(f"The number {num} is even.")
else:
  print(f"The number {num} is odd.")