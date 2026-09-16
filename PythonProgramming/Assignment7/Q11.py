#11. Write a Python program to print the Fibonacci series using recursion.
def fibonacci(n):
  if n==0:
    return 0
  elif n == 1 or n == 2:
    return 1
  return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Enter a range for fibonacci series "))
if n<0:
  print("Enter a positive range.")
else:
  print("The fibonacci series is")
  for i in range(n+1):
    print(fibonacci(i),end=" ")
    

'''
Enter a range for fibonacci series 5
The fibonacci series is
0 1 1 2 3 5 
'''