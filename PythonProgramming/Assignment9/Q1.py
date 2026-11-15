# Write a Python program that will search whether a particular word given by user is present in a file or not.

file = open("first.txt","r")
content = file.read()
word = input("Enter the word to find ").lower()
if word in content.lower():
  print(f"The word {word} is in the file.")
else:
  print(f"The word {word} is not in the file.")

file.close()

'''
Enter the word to find Python
The word python is in the file.
'''