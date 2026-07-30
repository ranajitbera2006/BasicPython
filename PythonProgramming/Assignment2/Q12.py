
num = int(input("Enter a positive number to sum its digits "))
while(1):
  num1 = num
  if(num1>0):
    result = 0
    while(num>0):
      rim = num%10
      result +=  rim
      num//=10
    print(f"The sum of the digits of the number {num1} is {result}.")
    break
  else:
    num = int(input("Please enter a positive number "))