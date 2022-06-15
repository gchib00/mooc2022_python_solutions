# Write your solution here
def even_numbers(list):
  even_nums = []
  for n in list:
    if n % 2 == 0:
      even_nums.append(n)
  return even_nums
if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  new_list = even_numbers(my_list)
  print("original", my_list)
  print("new", new_list)