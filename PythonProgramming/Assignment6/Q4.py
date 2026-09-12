#4. Create a list of 3 numbers and delete the second number from the list and print the updated list.

li = []
for i in range(3):
  li.append(i)
print("Before deleting ",li)
del li[1]
print("After deleting ",li)

'''
Before deleting  [0, 1, 2]
After deleting  [0, 2]
'''