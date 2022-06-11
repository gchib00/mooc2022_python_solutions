# Copy here code of line function from previous exercise
def line(size, string):
    if string == "":
        string = "*"
    print(size*string[0])
def triangle(size):
    i = 0
    row_size = 1
    while i < size:
        line(row_size, "#")
        i += 1
        row_size += 1
if __name__ == "__main__":
    triangle(5)