# Write your solution here
def longest_series_of_neighbours(list):
  arr = []
  counter = 0
  prevNum = None
  for n in list:
    if prevNum != None:
      if prevNum == n+1 or prevNum == n-1:
        counter += 1
      else:
        counter = 0
    arr.append(counter)
    prevNum = n
  return max(arr)+1
if __name__ == "__main__":
  my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  print(longest_series_of_neighbours(my_list))