'''
4. Take a positive number from the user to perform the following:
   (i) Calculate natural logarithm using math.log().
   (ii) Calculate logarithm with base 10 using math.log10().
   (iii) Calculate logarithm with custom base using math.log(x, base).
'''
import math as m
a = int(input("Enter a positive number "))
print(f"log{a} = {m.log(a)}")
print(f"log10{a} = {m.log10(a)}")
b = int(input("Enter the base "))
print(f"log{b}{a} = {m.log(a,b)}")

'''
Enter a positive number 100
log100 = 4.605170185988092
log10100 = 2.0
Enter the base 10
log10100 = 2.0
'''
