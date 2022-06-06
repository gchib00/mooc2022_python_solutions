# Write your solution here
word = input("Please type in a string:")
char = input("Please type in a character:")
index = word.find(char)
while index < len(word):
    strFragment = word[index:index+3]
    if len(strFragment) == 3 and strFragment[0] == char:
        print(word[index:index+3])
    index += 1