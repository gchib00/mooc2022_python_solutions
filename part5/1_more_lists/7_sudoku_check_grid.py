# Write your solution here
def row_correct(sudoku: list, row_no: int):
  arr = []
  for n in sudoku[row_no]:
    if n != 0 and n in arr:
      return False
    arr.append(n)
  return True
def column_correct(sudoku: list, column_no: int):
  arr = []
  for row in sudoku:
    if row[column_no] != 0 and row[column_no] in arr:
      return False
    arr.append(row[column_no])
  return True
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
def sudoku_grid_correct(sudoku: list):
  special_indices = [0, 3, 6]
  for i in range(len(sudoku)):
    if row_correct(sudoku, i) == False:
      return False
    for ii in range(len(sudoku[i])):
      if column_correct(sudoku, ii) == False:
        return False
      if i in special_indices and ii in special_indices:
        if block_correct(sudoku, i, ii) == False:
          return False
  return True

if __name__ == "__main__":
  sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]
  sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
  ]
  print(sudoku_grid_correct(sudoku1))
  print(sudoku_grid_correct(sudoku2))