#6. Write a program that prompts the user to input a number. Program should display the corresponding days to the number. For example, if user type 1 the output should be Sunday. If user type 7, the output should be Saturday.

ch = int(input("Enter a number (1 tp 7) to print corrospond day "))
while(1):

  if(ch>=1 and ch<=7):

    if(ch==1):
      print("Sunday")
    elif(ch==2):
      print("Monday")
    elif(ch==3):
      print("Tuesday")
    elif(ch==4):
      print("Wednesday")
    elif(ch==5):
      print("Thursday")
    elif(ch==6):
      print("Friday")
    elif(ch==7):
      print("Saturday")
    break
  else:
    ch = int(input("Please enter a valid number (1 to 7) "))