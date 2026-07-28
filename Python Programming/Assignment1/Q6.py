#6. Write a program that prompts the user to input the radius of a circle and outputs the area and circumference of the circle.

rad = float(input("Enter the radius of the circle "))
area = 3.14* rad**2
circum = 2*3.14*rad
print(f"The area of the circle is {area}")
print(f"The circumferance fo the circle is {circum}")
