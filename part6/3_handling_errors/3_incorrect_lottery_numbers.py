# Write your solution here
def filter_incorrect():
  data = []
  filtered_data = []
  with open("lottery_numbers.csv") as file:
    for line in file:
      data.append(line.replace("\n", ""))
  for line in data:
    week = line[5:].split(";")[0]
    lottery_numbers = line[5:].split(";")[1].split(",")
    try:
      if int(week) < 1:
        continue
      if len(lottery_numbers) != 7:
        continue
      for i in range(len(lottery_numbers)):
        lottery_numbers[i] = int(lottery_numbers[i])
      for lot_num in lottery_numbers:
        appeared = 0
        if lot_num > 39 or lot_num < 1:
          raise ValueError
        for lot_num2 in lottery_numbers:
          if lot_num2 == lot_num:
            appeared += 1
        if appeared > 1:
          raise ValueError
      filtered_data.append(line)
    except:
      pass
  with open("correct_numbers.csv", "w") as file:
    for line in filtered_data:
      file.write(line + "\n")
