# Write your solution here
integer = int(input("Please type in a positive integer:"))
for n in range((integer)*-1, integer+1):
  if n != 0:
    print(n)