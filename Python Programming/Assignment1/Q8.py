
a = float(input("Please enter the first side of the triangle "))
b = float(input("Please enter the second side of the triangle "))
c = float(input("Please enter the third side of the triangle "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"The area of the triangle is {area}")