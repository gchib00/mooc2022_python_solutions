# Write your solution here
word = input("Please type in a string:")
char = input("Please type in a character:")
index = word.find(char)
strFragment = word[index:index+3]
if len(strFragment) == 3:
    print(word[index:index+3])