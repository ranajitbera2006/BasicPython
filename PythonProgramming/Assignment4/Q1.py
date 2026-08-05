#1. Write a Python program to find the 2nd largest number from the list of the numbers entered through keyboard.
li = []
size = int(input("Enter the size of the list "))
print("Enter the elements of the list ")
for i in range(size):
  li.append(int(input()))
large = max(li)
for i in range(size):
  if large == max(li):
    li.remove(large)
print(f"The second largest element of the list is {max(li)}.")
