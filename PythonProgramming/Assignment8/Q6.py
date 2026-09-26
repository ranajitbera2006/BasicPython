#6. Write a Python program that first generates a random number between 1 to 50 using the random module. Then ask the user to guess the randomly generated number. If the guess matches, display a congratulatory message. If the guess is greater than the number, inform the user that the guess is too high, and if it is lower, inform the user that the guess is too low.
import random as r
com = r.randint(1,50)
gs = int(input("Enter your guess (1 to 50) "))
if gs>com:
  print("Your guess is high.")
elif gs<com:
  print("Your guess is lower.")
else:
  print("Congratulation! Your guess number matched.")
print("Generate number is",com)

'''
Enter your guess (1 to 50) 45
Your guess is high.
Generate number is 31
'''