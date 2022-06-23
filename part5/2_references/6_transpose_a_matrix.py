# Write your solution here
def transpose(matrix: list):
  matrix_copy = []
  for i in range(len(matrix)):
    arr = []
    for row in matrix:
      arr.append(row[i])  
    matrix_copy.append(arr)
  for i in range(len(matrix_copy)):
    matrix[i] = matrix_copy[i][:]
  print(matrix)
if __name__ == "__main__":
  transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])