# Write your solution here
def count_matching_elements(m, target):
  counter = 0
  for row in m:
    for n in row:
      if n == target:
        counter += 1
  return counter
if __name__ == "__main__":
  m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
  print(count_matching_elements(m, 1))