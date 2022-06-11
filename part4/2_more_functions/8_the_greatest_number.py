# Write your solution here
def greatest_number(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n3:
        return n2
    return n3
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)