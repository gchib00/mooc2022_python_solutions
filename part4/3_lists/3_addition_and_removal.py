# Write your solution here
arr = []
number = 1
while True:
  print("The list is now", arr)
  input_type = input("a(d)d, (r)emove or e(x)it:")
  if input_type == "d":
    arr.append(number)
    number += 1
  elif input_type == "r":
    arr.pop(-1)
    number -= 1
  elif input_type == "x":
    print("Bye!")
    break