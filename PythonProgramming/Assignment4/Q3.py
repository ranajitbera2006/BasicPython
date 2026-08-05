#3. Write a Python program to calculate mean of a given list of numbers.
li = []
size = int(input("Enter the size of the list "))
print("Enter the elements of the list ")
for i in range(size):
  li.append(int(input()))
mean = sum(li)/size
print(f"The mean of ther list of the numbers is {mean}")
