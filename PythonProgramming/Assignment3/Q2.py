#2. Write a program that prompts the user to enter a number n, and then prints all the odd numbers between 1 and n.
num = int(input("Enter a number "))
print(f"The series of odd number from 1 to {num} is ")
for i in range(1,num+1):
  if(i%2 != 0):
    print(i,end=" ")