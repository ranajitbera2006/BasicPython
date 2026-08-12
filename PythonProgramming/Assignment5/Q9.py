#9. Write a Python program to access age and company from above dictionary.
emp = {}
n = int(input("Enter the number of items "))
for i in range(n):
  key = input("Enter key ").lower()
  value = input("Enter value ")
  if(value.isdigit()):
    value = int(value)
  emp[key] = value
print(f"Age: {emp.get('age')}\nSalary: {emp.get('salary')}.")


'''
Output
Enter the number of items 4
Enter key name
Enter value Ranajit Bera
Enter key age
Enter value 19
Enter key salary
Enter value 50000
Enter key company
Enter value TCS
Age: 19
Salary: 50000.
'''