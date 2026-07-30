
char = input("Please a character ")
ch = char.lower()
if(char.isalpha()):
  if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(f"{char} is a vowel.")
  else:
    print(f"{char} is a consonant.")
else:
  print("It is not an alphabate.")    