'''
3. Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule:

Minimum Rs. 200 for up to 100 calls.
Plus Rs. 0.60 per call for next 50 calls.
Plus Rs. 0.50 per call for next 50 calls.
Plus Rs. 0.40 per call for any call beyond 200 calls.
'''

calls = int(input("Enter the numbers of calls "))
bill = 0
if(calls<=100):
  bill = 200
elif(calls<=150):
  bill = 200 + (calls-100)*0.60
elif(calls<=200):
  bill = 200 + (calls-100)*0.60 + (calls-150)*0.50
else:
  bill = 200 + (calls-100)*0.60 + (calls-150)*0.50 + (calls-200)*0.40 
print(f"Your total bill is {bill} rs.")