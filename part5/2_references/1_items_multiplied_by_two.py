# Write your solution here
def double_items(numbers):
  new_arr = []
  for n in numbers:
    new_arr.append(n*2)
  return new_arr
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)