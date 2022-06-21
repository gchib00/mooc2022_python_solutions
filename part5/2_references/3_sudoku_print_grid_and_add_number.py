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
  print_sudoku(sudoku)
  add_number(sudoku, 0, 0, 2)
  add_number(sudoku, 1, 2, 7)
  add_number(sudoku, 5, 7, 3)
  print()
  print("Three numbers added:")
  print()
  print_sudoku(sudoku)
