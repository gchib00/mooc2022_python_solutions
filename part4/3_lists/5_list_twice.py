# Write your solution here
arr = []
while True:
  num = int(input("New item:"))
  if num == 0:
    break
  arr.append(num)
  print("The list now:", arr)
  print("The list in order:", sorted(arr))
print("Bye!")