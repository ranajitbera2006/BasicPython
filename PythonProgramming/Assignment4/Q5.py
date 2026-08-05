#5. Write Python program to remove duplicate elements from list.
size = int(input("Enter the size of the list "))
print("Enter the elements of the list ")
li = [int(input()) for _ in range(size)]
print("The list before operation is ",li)
li = list(dict.fromkeys(li))
print("The list after operation is ",li)
