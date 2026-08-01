#10. Write a program that input a list, repeat it twice and then print it.
li = []
size = int(input("Enter the size of the list "))
print("Enter the element of the list ")
for i in range(0,size):
  num = int(input())
  li.append(num)
print(li*2)