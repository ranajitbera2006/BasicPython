#4. Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number or not.
count = 0
num = int(input("Please Enter a positive number "))
for i in range(1,num+1):
  if(num%i==0):
    count+=1
  if(count == 3):
    break
if(count == 2):
  print(f"The number {num} is prime number.")
else:
  print(f"The number {num} is not a prime number.")
