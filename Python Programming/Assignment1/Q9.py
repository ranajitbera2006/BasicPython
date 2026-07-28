#9. Write a program that prompts the user to input the length and the width of a rectangle and outputs the area and perimeter of the rectangle. The formula is— Area = Length x Width, Perimeter = 2 x (Length + Width)

length = float(input("Please enter the length of the rectangle "))
width = float(input("Please enter the width of the rectangle "))
area = length*width
perimeter = 2*(length+width)
print(f"The area of the rectangle is {area}\nThe perimeter of the rectangle is {perimeter}")
