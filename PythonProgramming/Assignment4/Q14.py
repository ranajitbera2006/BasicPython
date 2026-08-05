#14. Write a program that counts the occurrences of a character in a string. Do not use built in count function.
string = input("Enter a string ")
char=0
for i in string:
  if(i.isspace() or i.isdigit()):
    pass
  else:
    char+=1
print("The character in the string is ",char)