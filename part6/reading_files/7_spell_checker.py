# write your solution here
string = input("Write text:").split(" ")
acceptable_words = []

with open("wordlist.txt") as file:
  for line in file:
    line = line.replace("\n", "")
    acceptable_words.append(line)

for i in range(len(string)):
  if string[i].lower() not in acceptable_words:
    string[i] = "*"+string[i]+"*"

string = " ".join(string)
print(string)