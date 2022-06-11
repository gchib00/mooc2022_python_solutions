# Copy here code of line function from previous exercise and use it in your solution
def line(size, string):
    if string == "":
        string = "*"
    print(size*string[0])
def shape(tr_size, tr_char, rt_height, rt_char):
    # draw triangle:
    i = 0
    while i <= tr_size:
        line(i, tr_char)
        i += 1
    #draw recrangle:
    i = 0
    while i < rt_height:
        line(tr_size, rt_char)
        i += 1
if __name__ == "__main__":
    shape(5, "x", 2, "o")