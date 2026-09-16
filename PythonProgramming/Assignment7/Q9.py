#9. Write a program in Python to display the value of local and global variable using function.
n = "Hello world"
def display():
  n1 = 100
  global n
  n = "Hello India"
  print("Inside fn local variable value is:",n1)
  print(f"Global variable value is {n}")
print(f"Global variable value before fn call is",n)
display()

'''
Global variable value before fn call is Hello world
Inside fn local variable value is: 100
Global variable value is Hello India
'''