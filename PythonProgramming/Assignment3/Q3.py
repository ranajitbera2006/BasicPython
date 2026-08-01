#3. Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered.
pos = 0
neg = 0
zero = 0
while(1):
  ch = input("Are you want to input any number (yes->y & no->n) ")
  if(ch == 'y'):
    num = int(input("Enter a number "))
    if(num>0):
      pos +=1
    elif(num==0):
      zero +=1
    else:
      neg +=1
  elif(ch == 'n'):
    break
  else:
    print("Please enter (yes->y & no->n).")

print(f"The number of positive number is {pos}.")
print(f"The number of Negetive number is {neg}.")
print(f"The number of zero number is {zero}.")