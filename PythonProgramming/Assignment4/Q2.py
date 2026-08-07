#2. Write a Python program to search for an element in a given list of numbers.
li = []
size = int(input("Enter the size of the list "))
print("Enter the elements of the list ")
found = 0
for i in range(size):
  li.append(int(input()))
num = int(input("Enter a number to find "))
for i in li:
  if i == num:
    found+=1
if found>0:
  print(f"The number {num} is found.")
else:
  print("The number is not found.")
