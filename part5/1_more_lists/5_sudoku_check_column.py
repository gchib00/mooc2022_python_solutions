# Write your solution here
def column_correct(sudoku: list, column_no: int):
  arr = []
  for row in sudoku:
    if row[column_no] != 0 and row[column_no] in arr:
      return False
    arr.append(row[column_no])
  return True