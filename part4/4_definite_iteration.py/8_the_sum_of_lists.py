# Write your solution here
def list_sum(list1, list2):
  new_arr = []
  i = 0
  while i < len(list1):
    new_arr.append(list1[i] + list2[i])
    i += 1
  return new_arr
if __name__ == "__main__":
  a = [1, 2, 3]
  b = [7, 8, 9]
  print(list_sum(a, b)) # [8, 10, 12]