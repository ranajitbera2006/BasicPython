#8. Suppose a, b, and c denote the lengths of the sides of a triangle. Then the area of the triangle can be calculated using the formula: Area = sqrt(s * (s - a) * (s - b) * (s - c)) where s = (a + b + c) / 2. Write a program that asks the user to input the length of sides of the triangle and print the area.

a = float(input("Please enter the first side of the triangle "))
b = float(input("Please enter the second side of the triangle "))
c = float(input("Please enter the third side of the triangle "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"The area of the triangle is {area}")