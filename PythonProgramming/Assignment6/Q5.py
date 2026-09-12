#5. Write a program in Python to find common elements from the two list.

li1 = []
li2 = []

for i in range(5):
  li1.append(i)
for i in range(3,7):
  li2.append(i)
print(f"li1 : {li1}\nli2: {li2}")
li3 = set(li1) & set(li2)
print(f"Common in li1 & li2 {list(li3)}")

'''
li1 : [0, 1, 2, 3, 4]
li2: [3, 4, 5, 6]
Common in li1 & li2 [3, 4]
'''