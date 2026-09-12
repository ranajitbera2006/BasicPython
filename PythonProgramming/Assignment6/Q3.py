#3. Write a program to concatenate two list using extend functions.

li1 = []
li2 = []
for i in range(3):
  li1.append(i)
for i in range(4,8):
  li2.append(i)

li1.extend(li2)
print(li1)


'''
[0, 1, 2, 4, 5, 6, 7]
'''