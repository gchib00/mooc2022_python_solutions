# Write your solution here
def distinct_numbers(list):
  new_arr = []
  for num in list:
    if num not in new_arr:
      new_arr.append(num)
  return sorted(new_arr)
if __name__ == "__main__":
  my_list = [3, 2, 2, 1, 3, 3, 1, 8]
  print(distinct_numbers(my_list))