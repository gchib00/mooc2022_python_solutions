# Write your solution here
def row_correct(sudoku: list, row_no: int):
  arr = []
  for n in sudoku[row_no]:
    if n != 0 and n in arr:
      return False
    arr.append(n)
  return True