# Write your solution here
word = input("Word:")
row = "*" * 30
central_row_side1 = "*" + " " * int((29 - len(word)) / 2)
central_row_side2 = " " * int((28 - len(word)) / 2) + "*"
central_row = central_row_side1 + word + central_row_side2

print(row)
print(central_row)
print(row)