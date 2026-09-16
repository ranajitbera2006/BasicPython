#10. Write a Python program to find out factorial of a number using recursion.
def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n*factorial(n-1)
n = int(input("Enter a number "))
if n<0:
  print("Enter a positive number.")
else:
  print(f"{n} ! = {factorial(n)}")

'''
Enter a number 5
5 ! = 120
'''