#10. Write a Python program to take input from the user and then check whether it is a number or a character, determine whether it is in uppercase or lowercase.
enter = input("Enter any input ")
if(enter.isdigit()):
  print("The input is number.")
else:
  if(enter.isupper()):
    print("The input is in upper case.")
  elif(enter.islower()):
    print("The input is in lower case.")
  else:
    print("The input contains both upper and lower case.")
  