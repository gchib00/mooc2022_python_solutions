# Write your solution here
def formatted(list):
  new_arr = []
  for n in list:
    new_arr.append(f"{n:.2f}")
  return new_arr
if __name__ == "__main__":
  my_list = [1.234, 0.3333, 0.11111, 3.446]
  new_list = formatted(my_list)
  print(new_list)