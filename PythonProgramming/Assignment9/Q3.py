#Write even and odd numbers to separate files. Create a program that: Reads numbers from a list, writes even numbers to even.txt and odd number to odd.txt file. Display the contents of both files.

li = [1,2,3,4,5,6,7,8,9,10]
with open("even.txt","a+") as even_file, open("odd.txt","a+") as odd_file:
  for el in li:
    if el%2 == 0:
      even_file.write(f"{el}\n")
    else:
      odd_file.write(f"{el}\n")

  even_file.seek(0)
  odd_file.seek(0)
  even_content = even_file.read()
  odd_content = odd_file.read()

  print(f"Even file contents:\n{even_content}")
  print(f"Odd file contents:\n{odd_content}")


'''
Even file contents:
2
4
6
8
10

Odd file contents:
1
3
5
7
9

'''