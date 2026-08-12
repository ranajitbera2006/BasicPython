#11. Given a dictionary where keys are employee names and values are tuples (age, salary), write a program to sort the dictionary items based on the salary in ascending order.
emp = {
  "Ram":(30,50000),
  "Rani":(25,45000),
  "Sam":(32,75000)
}
sorted_emp = sorted(emp.items(),key=lambda e:e[1][1])
sorted_emp = dict(sorted_emp)
print("The sorted dictionary on the base of salary is\n",sorted_emp)



'''
Output
The sorted dictionary on the base of salary is
 {'Rani': (25, 45000), 'Ram': (30, 50000), 'Sam': (32, 75000)}
'''