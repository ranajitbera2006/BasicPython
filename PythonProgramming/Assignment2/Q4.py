
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
