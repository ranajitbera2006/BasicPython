'''2. Write a program that prompts the user to input a year and determine whether the year is a leap year or not.

1992 Leap Year
2000 Leap Year
1900 NOT a Leap Year
1995 NOT a Leap Year'''

year = int(input("Enter the year "))
if((year%4 == 0 and year%100 != 0 )or year%400 == 0):
  print(f"The year {year} is Leap year.")
else:
  print(f"The year {year} is not Leap year.")