# Write your solution here
def factorials(n: int):
  directory = {}
  i = 1
  factorial = 1
  for number in range(n):
    if number == 0:
      directory[1] = 1
    else:
      directory[i] = i * factorial
      factorial = directory[i]
    i += 1
    print(number)
  return directory
if __name__ == "__main__":
  k = factorials(5)
  print(k)
  print(k[1])
  print(k[3])
  print(k[5])