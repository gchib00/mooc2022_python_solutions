# Write your solution here
def dict_of_numbers():
  dict = {}
  list1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  list2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  list3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  i = 0
  if i < 20:
    while i < 10:
      dict[i] = list1[i]
      i += 1
    while i >= 10 and i < 20:
      second_digit = str(i)[1]
      dict[i] = list2[int(second_digit)]
      i += 1 
  if i > 19:
    while i >= 20 and i < 100:
      first_digit = int(str(i)[0]) - 2
      second_digit = int(str(i)[1])
      if second_digit == 0:
        dict[i] = list3[first_digit]
      else:
        dict[i] = list3[first_digit] + "-" + list1[second_digit]
      i += 1
  return dict
if __name__ == "__main__":
  numbers = dict_of_numbers()
  print(numbers[2])
  print(numbers[11])
  print(numbers[45])
  print(numbers[99])
  print(numbers[0])