# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    row = "*"
    while i <= size:
        if i > 1:
            row += "**"
        margin = (size-i) * " "
        print(margin + row + margin)
        i += 1
    margin = (size-1) * " "
    print(margin + "*" + margin)
if __name__ == "__main__":
    spruce(5)