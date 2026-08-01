#12. Write a python program to check whether it contains same number in adjacent position and display the count of such adjacent occurrences.
li = [2,2,5,4,6,5,5]
count = 0
n = len(li)
for i in range(0,n-1):
  if(li[i] == li[i+1]):
    count+=1

print("The number of similar adjacent element ",count)