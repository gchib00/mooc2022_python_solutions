# Write your solution here
size = int(input("How many items: "))
arr = []
counter = 1
while counter <= size:
  value = int(input(f"Item {counter}: "))
  arr.append(value)
  counter += 1
print(arr)