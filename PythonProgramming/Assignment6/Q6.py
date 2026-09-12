#6. Create a nested list containing only integers. Then display the updated list after removing the last elements of each sub lists.

li = list(eval(input("Enter the nested lists ")))
print("The list is ",li)
for i in li:
  i.pop()
print("After deleting the last element from each nested list is",li)

'''
Enter the nested lists [1,2,3],[6,7,9]
The list is  [[1, 2, 3], [6, 7, 9]]
After deleting the last element from each nested list is [[1, 2], [6, 7]]
'''