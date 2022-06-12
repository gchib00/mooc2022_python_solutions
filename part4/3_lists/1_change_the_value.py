# Write your solution here
arr = [1, 2, 3, 4, 5]

while True:
  index = int(input("Index:"))
  if index == -1:
    break
  new_val = int(input("New value:"))
  arr[index] = new_val
  print(arr)