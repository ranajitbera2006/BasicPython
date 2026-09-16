#13. Write a Python program to find minimum number between two numbers using Lambda function.
min_from_two = lambda a,b:a if a<=b else b
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(f"Minimum from {a} and {b} is {min_from_two(a,b)}.")

'''
Enter the first number 1
Enter the second number 2
Minimum from 1 and 2 is 1.
'''