#1. Create a list of 7 numbers and print the list from the first element to last element using step size 2 and for loop.

li = []
li1 = []
for i in range(7):
  li.append(i)
print(li)
for i in range(1,7,2):
  li1.append(li[i])
print(li1)

'''
[0, 1, 2, 3, 4, 5, 6]
[1, 3, 5]
'''