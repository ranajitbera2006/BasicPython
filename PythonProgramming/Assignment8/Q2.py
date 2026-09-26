#2. Build a simple trigonometric calculator that takes an angle in degrees from the user, converts it to radians using math.radians(), and calculates and displays sin, cos, and tan values. Also calculate their inverse functions (asin, acos, atan).
import math as m
angle_deg = int(input("Enter the angle in degree "))
angle_rad = m.radians(angle_deg)
print(f"sin({angle_rad}) = {m.sin(angle_rad)}")
print(f"cos({angle_rad}) = {m.cos(angle_rad)}")
print(f"tan({angle_rad}) = {m.tan(angle_rad)}")
print(f"sin^-1({angle_rad}) = {m.asin(angle_rad)}")
print(f"cos^-1({angle_rad}) = {m.acos(angle_rad)}")
print(f"tan^-1({angle_rad}) = {m.atan(angle_rad)}")

'''
Enter the angle in degree 0
sin(0.0) = 0.0
cos(0.0) = 1.0
tan(0.0) = 0.0
sin^-1(0.0) = 0.0
cos^-1(0.0) = 1.5707963267948966
tan^-1(0.0) = 0.0
'''