
num = int(input("Enter a positive number to factorial "))
while(1):
  if(num>=0):
    fact = 0
    if(num>0):
      for i in range(1,num+1):
        fact+=i
    print(f"{num}! = 1")
    break
  else:
    num = int(input("Please enter a positive number "))