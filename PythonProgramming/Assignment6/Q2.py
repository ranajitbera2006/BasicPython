#2. Print the list of 5 elements from 3rd rightmost element to 2nd rightmost element using negative indexing.

li = []
for i in range(5):
  li.append(i)
print(li)
print(li[-3:-1])

'''
[0, 1, 2, 3, 4]
[2, 3]
'''