# Write your solution here
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
layers = int(input("Layers:"))
size = (layers * 2) - 1

# Create an empty matrix:
matrix = []
for i in range(size):
  row = []
  for ii in range(size):
    row.append(0)
  matrix.append(row)

# Populate the matrix:
ltr_index = 1
for i in range(size):
  for ii in range(size):
    if i == (layers - 1) and ii == (layers - 1):
      matrix[i][ii] = ltr_index
      ltr_index += ltr_index
      helper_i = 1
      while helper_i < layers:
        matrix[i][ii+helper_i] = ltr_index
        matrix[i][ii-helper_i] = ltr_index
        matrix[i+helper_i][ii] = ltr_index
        matrix[i-helper_i][ii] = ltr_index
        matrix[i+helper_i][ii+helper_i] = ltr_index
        matrix[i+helper_i][ii-helper_i] = ltr_index
        matrix[i-helper_i][ii-helper_i] = ltr_index
        matrix[i-helper_i][ii+helper_i] = ltr_index
        helper_i += 1
        ltr_index += 1
  for i in range(size):
    for ii in range(size):
      if (i == 0 or i == size-1) or (ii == 0 or ii == size-1):
        matrix[i][ii] = layers
      if matrix[i][ii] == 0 and i > ii:
        matrix[i][ii] = layers - ii
        matrix[i][-ii] = layers+1 - ii #+1
        matrix[-i][ii] = layers - ii
        matrix[-i][-ii] = layers+1 - ii #+1
      elif matrix[i][ii] == 0 and i < ii:
        matrix[i][ii] = layers - i 
        matrix[i][-ii] = layers - i
        matrix[-i][ii] = layers+1 - i #+1 
        matrix[-i][-ii] = layers+1 - i #+1
      elif matrix[i][ii] == 0 and i == ii:
        matrix[i][ii] = layers+1 - i
        matrix[i][-ii] = layers+1 - i
        matrix[-i][ii] = layers+1 - i
        matrix[-i][-ii] = layers+1 - i
    
# Translate matrix to alphabet:
alphabet_matrix = []
for row in matrix:
  new_row = ""
  for number in row:
    new_row += alphabet[number-1]
  alphabet_matrix.append(new_row)

# Print the matrix:
for row in alphabet_matrix:
  print(row)