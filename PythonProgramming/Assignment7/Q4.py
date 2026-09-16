#4. Write a Python program to find the greatest number from three numbers using function.
def largest(a,b,c):
  if a>=b and a>=c:
    return a
  elif b>=c:
    return b
  else:
    return c
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))
print(f"The largest number from {a,b,c} is {largest(a,b,c)}.")

'''
Enter the first number 1
Enter the second number 2
Enter the third number 3
The largest number from (1, 2, 3) is 3.
'''