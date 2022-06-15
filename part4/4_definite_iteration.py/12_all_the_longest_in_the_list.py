# Write your solution here
def all_the_longest(list):
  longest = 0
  for item in list:
    if len(item) > longest:
      longest = len(item)
  new_arr = []
  for item in list:
    if len(item) == longest:
      new_arr.append(item)
  return new_arr

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]
  result = all_the_longest(my_list)
  print(result)
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = all_the_longest(my_list)
  print(result)