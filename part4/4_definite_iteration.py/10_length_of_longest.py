# Write your solution here
def length_of_longest(list):
  longest = 0
  for item in list:
    if len(item) > longest:
      longest = len(item)
  return longest

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]
  result = length_of_longest(my_list)
  print(result)
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = length_of_longest(my_list)
  print(result)