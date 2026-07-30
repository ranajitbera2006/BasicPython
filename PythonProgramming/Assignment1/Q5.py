#5. Write a program that prompts the user to input a Celsius temperature and outputs the equivalent temperature in Fahrenheit. The formula to convert the temperature is: F = 9/5 * C + 32, where F is the Fahrenheit temperature and C is the Celsius temperature.

temp_in_cel = float(input("Enter the temperature in celsius "))
temp_in_far =(9/5 * temp_in_cel)+32
print(f"The temperature in fahrenheit is {temp_in_far}")