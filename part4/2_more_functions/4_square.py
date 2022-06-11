# Copy here code of line function from previous exercise
def line(size, string):
    if string == "":
        string = "*"
    print(size*string[0])
def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1
if __name__ == "__main__":
    square(5, "x")