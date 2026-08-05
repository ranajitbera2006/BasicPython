#4. Write a Python program to find minimum element from a list of elements along with its index in the list.
li = []
size = int(input("Enter the size of the list "))
print("Enter the elements of the list ")
for i in range(size):
  li.append(int(input()))
minimum = min(li)
index = li.index(minimum)
print(f"The minimum element of the list is {minimum} at the index {index}.")