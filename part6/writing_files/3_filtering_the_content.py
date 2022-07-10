# Write your solution here
def filter_solutions():
  with open("incorrect.csv", "w") as file:
    pass
  with open("correct.csv", "w") as file:
    pass
  with open("solutions.csv") as file:
    for line in file:
      line = line.split(";")
      if len(line) < 3:
        continue
      if "+" in line[1]:
        operands = line[1].split("+")
        if int(operands[0]) + int(operands[1]) == int(line[2]):
          with open("correct.csv", "a") as file2:
            file2.write(";".join(line))
        else:
          with open("incorrect.csv", "a") as file2:
            file2.write(";".join(line))
      else:
        operands = line[1].split("-")
        if int(operands[0]) - int(operands[1]) == int(line[2]):
          with open("correct.csv", "a") as file2:
            file2.write(";".join(line))
        else:
          with open("incorrect.csv", "a") as file2:
            file2.write(";".join(line))
filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()