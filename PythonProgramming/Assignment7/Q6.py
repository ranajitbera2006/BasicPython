#6. Write a Python program to find out the given number is odd or even using function.
def even_or_odd(n):
  if n%2==0:
    print(f"The number {n} is even.")
  else:
    print(f"The number {n} is odd.")
n = int(input("Enter the number "))
even_or_odd(n)

'''
Enter the number 5
The number 5 is odd.
'''