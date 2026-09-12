'''
8. Create an empty dictionary and add some names to the 0th, 1st and 2nd index.
i) Add another name in the third index.
ii) Delete the second index name.
'''

dic = {}

for i in range(3):
  key = i
  value = input(f"Enter the name{i} ")
  dic[key] = value
print(dic)
#1
dic[3] = input("Enter the 3rd index name ")
print(dic)
#2
print("Dic with deleted 2nd index")
del dic[2]
print(dic)


'''
Enter the name0 Ram
Enter the name1 Raj
Enter the name2 Raju
{0: 'Ram', 1: 'Raj', 2: 'Raju'}
Enter the 3rd index name Ramu
{0: 'Ram', 1: 'Raj', 2: 'Raju', 3: 'Ramu'}
Dic with deleted 2nd index
{0: 'Ram', 1: 'Raj', 3: 'Ramu'}
'''