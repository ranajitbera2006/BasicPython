#2. Write a Python program to calculate sum of digit of a number using function.
def sum_of_digits(n):
  result = 0
  while n != 0:
    rim = n%10
    result += rim
    n //= 10
  return result
n = int(input("Enter the number to find the sum of its digits "))
print(f"The sum of digits of {n} is {sum_of_digits(n)}.")

'''
Enter the number to find the sum of its digits 123
The sum of digits of 123 is 6.
'''