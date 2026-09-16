#7. Write a Python program to find out factorial of a number using function.
def factorial(n):
  fact = 1
  if n==0:
    return fact
  elif n<0:
    print("Enter a positive number.")
  else:
    for i in range(1,n+1):
      fact *= i
    return fact
n = int(input("Enter a number "))
if n>=0:
  print(f"{n} ! = {factorial(n)}")
else:
  factorial(n)

'''
Enter a number 5
5 ! = 120
'''