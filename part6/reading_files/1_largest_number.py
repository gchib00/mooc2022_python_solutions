# write your solution here
def largest():
  with open("numbers.txt") as file:
    list = []
    for num in file:
      list.append(int(num))
    return max(list)