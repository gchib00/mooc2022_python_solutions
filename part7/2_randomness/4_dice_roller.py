# Write your solution here
from random import randint

def roll(die: str):
  a = [3, 3, 3, 3, 3, 6]
  b = [2, 2, 2, 5, 5, 5]
  c = [1, 4, 4, 4, 4, 4]
  if die == "A":
    return a[randint(0, len(a)-1)]
  if die == "B":
    return b[randint(0, len(b)-1)]
  if die == "C":
    return c[randint(0, len(c)-1)]

def play(die1: str, die2: str, times: int):
  die1_wins = 0
  die2_wins = 0
  ties = 0
  for i in range(times):
    res1 = roll(die1)
    res2 = roll(die2)
    if res1 > res2:
      die1_wins += 1
    elif res1 < res2:
      die2_wins += 1
    else:
      ties += 1
  return (
    die1_wins,
    die2_wins,
    ties
  )