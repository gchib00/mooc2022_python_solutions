# Write your solution here
from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
  num_pool = list(range(lower, upper))
  shuffle(num_pool)
  draw = num_pool[0:amount]
  draw.sort()
  return draw