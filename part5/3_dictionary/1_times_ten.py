# Write your solution here
def times_ten(n1, n2):
  dictionary = {}
  counter = n1
  while counter <= n2:
    dictionary[counter] = counter * 10
    counter += 1
  return dictionary
if __name__ == "__main__":
  d = times_ten(3, 6)
  print(d)