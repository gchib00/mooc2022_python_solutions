# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
  arr = []
  for i in range(3):
    row = sudoku[row_no + i]
    for ii in range(3):
      cell = row[column_no + ii] 
      if cell != 0 and cell in arr:
        return False
      arr.append(cell)
  return True