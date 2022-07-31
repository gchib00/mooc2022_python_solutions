# Write your solution here
from random import randint

def words(n: int, beginning: str):
  data = []
  with open("words.txt") as file:
    for line in file:
      data.append(line.replace("\n", ""))
  filtered_data = []
  for word in data:
    if word.startswith(beginning):
      filtered_data.append(word)
  if len(filtered_data) < n:
    raise ValueError
  randomized_data = []
  for i in range(n):
    word = filtered_data[randint(0, len(filtered_data))]
    if word not in randomized_data:
      randomized_data.append(word)
  return randomized_data