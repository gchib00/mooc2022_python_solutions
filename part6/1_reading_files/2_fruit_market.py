# write your solution here
def read_fruits():
  with open("fruits.csv") as file:
    fruits = {}
    for line in file:
      line = line.replace("\n", "")
      parts = line.split(";")
      fruit = parts[0]
      price = float(parts[1])
      fruits.update({
        fruit: price
      })
    return fruits