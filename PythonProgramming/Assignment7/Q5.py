#5. Write a Python program to calculate square of a number using function.
def square(n):
  return n**2
n = int(input("Enter the number to square it "))
print(f"{n}^2 = {square(n)}")

'''
Enter the number to square it 5
5^2 = 25
'''