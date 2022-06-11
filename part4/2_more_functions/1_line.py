# Write your solution here
def line(size, string):
    if string == "":
        string = "*"
    print(size*string[0])
if __name__ == "__main__":
    line(5, "x")