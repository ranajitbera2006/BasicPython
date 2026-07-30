'''
5. The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade. The student gets a grade as per following rules:

Average    Grade
90-100     A
80-89      B
70-79      C
60-69      D
0-59       F
'''
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

