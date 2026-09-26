'''
7. Write a Python program that generates a random password of length 8 or more. Ensure that it contains:
   (i) Uppercase letters (A to Z)
   (ii) Lowercase letters (a to z)
   (iii) Digits (0 to 9)
   (iv) Special symbols (@, #, !, $, *, /, etc.)
   Ensure that it should be a string.
'''
import string as s
import random as r
capital = s.ascii_letters.upper()
small = s.ascii_letters.lower()
sp_char = '@#$%^*'
digits = '0123456789'
password = [r.choice(capital),r.choice(small),r.choice(digits),r.choice(sp_char)]
gen = [r.choice(capital),r.choice(small),r.choice(digits)]
for i in range(5):
  password.append(r.choice(gen)) 
gen_pass = ''.join(map(str,password))
print("Your password is",gen_pass)

#Your password is Nn8@00Yii