#8. Suppose you have 'N' flavours of toppings that can be added to a coffee. Write a function in Python that takes the number of available flavours as input and returns the total number of different ways we can have our coffee. (Note that we can have coffee without any toppings or with different combination of toppings).
def coffee_type(n):
  return 2**n
n = int(input("Enter the number of the flavours "))
print(f"The number of the coffee type is {coffee_type(n)}.")

'''
Enter the number of the flavours 5
The number of the coffee type is 32.
'''