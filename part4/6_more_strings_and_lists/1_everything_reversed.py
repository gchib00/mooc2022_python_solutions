# Write your solution here
def everything_reversed(list):
  new_arr = []
  for item in list:
    new_arr.append(item[::-1])
  return new_arr[::-1]
if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)