#3. Write a Python program that displays all leap years from 2000-2025 using function.
def leap_year_list():
  print("The list of leap year from 2000-2025")
  for i in range(2000,2026):
    if((i%4 == 0 and i%100 != 0) or i%400 == 0):
      print(i)
leap_year_list()

'''
The list of leap year from 2000-2025
2000
2004
2008
2012
2016
2020
2024
'''