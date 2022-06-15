# Write your solution here
def shortest(list):
  shortest = list[0]
  for item in list:
    if len(item) < len(shortest):
      shortest = item
  return shortest

if __name__ == "__main__":
  my_list = ['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']
  result = shortest(my_list)
  print(result)