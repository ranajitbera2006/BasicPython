#8. Create a Dictionary of employee name, age, salary and company as keys and give values to those keys.
emp = {}
n = int(input("Enter the number of items "))
for i in range(n):
  key = input("Enter key ")
  value = input("Enter value ")
  if(value.isdigit()):
    value = int(value)
  emp[key] = value
print(emp)

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
{'name': 'Ranajit Bera', 'age': 19, 'salary': 50000, 'company': 'TCS'}
'''