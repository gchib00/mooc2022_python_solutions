# Write your solution here
def squared(string, size):
    combined_string = string * (size**2)
    combined_string = combined_string[:size**2]
    while len(combined_string) > 0:
        row = combined_string[:size]
        print(row)
        combined_string = combined_string[len(row):]

if __name__ == "__main__":
    squared("aybabtu", 5)