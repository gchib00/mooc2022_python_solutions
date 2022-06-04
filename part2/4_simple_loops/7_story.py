# Write your solution here
story = ""
prevWord = ""
while True:
    word = input("Please type in a word:")
    if word == "end" or prevWord == word:
        break
    else:
        prevWord = word
        story += word + " "
print(story)