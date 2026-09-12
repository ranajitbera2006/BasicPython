#10. Create a dictionary of employee's name, age, salary, company and sort the keys of the dictionary.

emp = {
  "name":"Ram",
  "age":34,
  "salary":50000,
  "company":"TCS"
}
sorted_emp = sorted(emp.items(),key=lambda e:e[0].lower())
sorted_emp = dict(sorted_emp)
print("Sorted dictionary by key ",sorted_emp)

# Sorted dictionary by key  {'age': 34, 'company': 'TCS', 'name': 'Ram', 'salary': 50000}