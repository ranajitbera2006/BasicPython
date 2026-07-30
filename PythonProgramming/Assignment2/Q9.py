#9. Write a program that asks the user for a positive integer value. The program should calculate the sum of all the integers from 1 up to the number entered. CO2

num = int(input("Enter a positive number to sum "))
while(1):
  if(num>0):
    sum = 0
    for i in range(1,num+1):
      sum+=i
    print(f"The sum of 1 to {num} is {sum}.")
    break
  else:
    num = int(input("Please enter a positive number "))