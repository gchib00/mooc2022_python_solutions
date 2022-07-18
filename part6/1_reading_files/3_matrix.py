# write your solution here
def matrix_sum():
  with open("matrix.txt") as file:
    numbers = []
    for row in file:
      row = row.replace("\n", "")
      row = row.split(",")
      for number in row:
        numbers.append(int(number))
    return sum(numbers)
def matrix_max():
  with open("matrix.txt") as file:
    numbers = []
    for row in file:
      row = row.replace("\n", "")
      row = row.split(",")
      for number in row:
        numbers.append(int(number))
    return max(numbers)
def row_sums():
  with open("matrix.txt") as file:
    list = []
    for row in file:
      row = row.replace("\n", "")
      row = row.split(",")
      row_sum = 0
      for number in row:
        row_sum += int(number)
      list.append(row_sum)
    return list