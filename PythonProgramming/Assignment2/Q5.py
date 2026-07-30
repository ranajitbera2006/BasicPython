
marks1 = int(input("Enter the first marks "))
marks2 = int(input("Enter the second marks "))
marks3 = int(input("Enter the third marks "))
avg = (marks1+marks2+marks3)/3
if(avg<=100 and avg>=90):
  print("Your grade is A.")
elif(avg<90 and avg>=80):
  print("Your grade is B.")
elif(avg<80 and avg>=70):
  print("Your grade is C.")
elif(avg<70 and avg>=60):
  print("Your grade is D.")
elif(avg<60 and avg>=0):
  print("Your grade is F.")
else:
  print("Please enter valid marks.")

