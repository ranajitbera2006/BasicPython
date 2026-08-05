#9. Write a Python program to check a given string is upper case or lower case.
string = "Ranajit"
if(string.isupper()):
  print("The string is in upper case.")
elif(string.islower()):
  print("The string is in lower case.")
else:
  print("The string contains both upper and lower case.")
  