# Write your solution here
sentence = input("Please type in a sentence:")

index = 0
while index < len(sentence):
    if index == 0 or sentence[index-1] == " ":
        print(sentence[index])
    index += 1