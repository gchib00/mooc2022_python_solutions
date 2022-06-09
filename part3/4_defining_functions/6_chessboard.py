# Write your solution here
def chessboard(num):
    i = 0
    while i < num:
        if i % 2 == 0:
            string = "10" * num
        else:
            string = "01" * num
        print(string[0:num])
        i += 1
if __name__ == "__main__":
    chessboard(3)
