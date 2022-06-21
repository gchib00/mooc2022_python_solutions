# Write your solution here
def print_sudoku(sudoku: list):
  row_index = 0
  for row in sudoku:
    row_string = ""
    column_index = 0
    for column in row:
      if column == 0 and column_index % 3 == 2:
        row_string += "_  "
      elif column != 0 and column_index % 3 == 2:
        row_string += str(column) + "  "
      elif column == 0:
        row_string += "_ "
      else:
        row_string += str(column) + " "
      column_index += 1
    if row_index % 3 == 0:
      print()
    row_index += 1
    print(row_string)
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
  sudoku[row_no][column_no] = number
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  new_grid = []
  for i in range(len(sudoku)):
    row = sudoku[i][:]
    new_grid.append(row)
  add_number(new_grid, row_no, column_no, number)
  return new_grid

if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)