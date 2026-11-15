# Student Marks Management: Maintain a student record named students.txt file. Program should: Add new student records (name, marks). Display all records, find the student with the highest marks.

import ast
name = input("Enter the name of the student ")
marks = int(input("Enter the marks of the student "))
newStudent = {
  "name":name,
  "marks":marks
}

with open("students.txt","a+") as file:
  file.write(f"{newStudent}\n")
  file.seek(0)
  contents = file.read().splitlines()
  print("Students record:")
  print(contents)
  max_marks = -1
  top_stu = ""
  for i in contents:
    if not i.strip():
      continue
    student = ast.literal_eval(i)
    if max_marks < student["marks"]:
      max_marks = student["marks"]
      top_stu = [student["name"]]
    elif max_marks == student["marks"]:
      top_stu.append(student["name"])
  print(f"The topper(s) is {', '.join(top_stu)} with {max_marks} marks.")
    

'''
Enter the name of the student Shyam Das
Enter the marks of the student 98
Students record:
["{'name':'Ram Das','marks':90}", "{'name': 'Shyam Das', 'marks': 98}"]
The topper(s) is Shyam Das with 98 marks.
'''