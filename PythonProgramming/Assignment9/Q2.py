#Count specific word frequency in a file. Create a file story.txt and add some text manually. Write a python program that: opens and reads the file, counts how many times a specific word (entered by the user) appears. Display the count.

c = 0
word = input("Enter the word ").lower()
with open("story.txt","r") as file:
  words = file.read().lower().split()
  for w in words:
    if w.strip(",.'\";:-!") == word:
      c += 1
print(f"The word {word} contains in the file {c} times.")

'''
Enter the word code
The word code contains in the file 2 times.
'''