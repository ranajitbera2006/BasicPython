'''
4. The roots of the quadratic equation ax^2 + bx + c = 0, a != 0 are given by the following formula:

In this formula, the term b^2 - 4ac is called the discriminant. If b^2 - 4ac = 0, then the equation has two equal roots. If b^2 - 4ac >= 0, the equation has two real roots. If b^2 - 4ac < 0, the equation has two complex roots.

Write a program that prompts the user to input the value of a (the coefficient of x^2), b (the coefficient of x), and c (the constant term) and outputs the roots of the quadratic equation.
'''
a = int(input("Enter the value of a (a != 0) "))
while(1):
  if(a==0):
    a = int(input("Enter a non-zero value of a "))
  else:
    break
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
discriminant = (b**2 - (4*a*c))
if(discriminant>=0):
  root1 = (-b + (discriminant)**0.5)/(2*a)
  root2 = (-b - discriminant)/(2*a)
  print(f"The roots of the equation are {root1} and {root2}.")
else:
  print("The roots of the equation are complex number.")
