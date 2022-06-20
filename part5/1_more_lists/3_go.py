# Write your solution here
def who_won(game_board: list):
  p1_score = 0
  p2_score = 0
  for row in game_board:
    for n in row:
      if n == 1:
        p1_score += 1
      elif n == 2:
        p2_score += 1
  if p1_score > p2_score:
    return 1
  elif p1_score < p2_score:
    return 2
  else:
    return 0