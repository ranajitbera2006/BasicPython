#6. Write a program that creates a list of number from 1 to 20 that are divisible by 4.
li = []
for i in range(1,21):
  if(i%4 == 0):
   print(i,end=" ")
