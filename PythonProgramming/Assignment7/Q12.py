#12. Write a Python program to add two numbers using Lambda function.
add_tow_number = lambda a,b:a+b
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(f"{a} + {b} = {add_tow_number(a,b)}")

'''
Enter the first number 1
Enter the second number 2
1 + 2 = 3
'''