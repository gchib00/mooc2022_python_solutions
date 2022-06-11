# Write your solution here
def same_chars(string, char1, char2):
    if char1 >= len(string) or char2 >= len(string):
        return False
    if string[char1] == string[char2]:
        return True
    return False
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))