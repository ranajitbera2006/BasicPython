'''
3. Create a program using the math module that:
   (i) Takes radius as input from the user.
   (ii) Calculates the area and circumference of a circle.
   (iii) Calculates the surface area and volume of a sphere.
   (iv) Uses math.pi for accurate calculations.
'''
import math as m
r = int(input("Enter the radius "))
print(f"The area and circumference of the circle is {m.pi*m.pow(r,2)} and {2*m.pi*r}.")
print(f"The surface and volume of the sphere is {4*m.pi*m.pow(r,2)} and {(4/3)*m.pi*m.pow(r,3)}.")

'''
Enter the radius 3
The area and circumference of the circle is 28.274333882308138 and 18.84955592153876.
The surface and volume of the sphere is 113.09733552923255 and 113.09733552923254.
'''