#11. Write a Python program to count uppercase, lowercases, space in a string.
up=0
lo=0
sp=0
string = input("Enter a string ")
for char in string:
  if(char.isupper()):
    up+=1
  elif(char.islower()):
    lo+=1
  elif(char.isspace()):
    sp+=1
print(f"The number of upper latter {up},lower latter {lo} and space {sp}.")