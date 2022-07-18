# Write your solution here
def find_words(search_term: str):
  words = []
  with open("words.txt") as file:
    for line in file:
      line = line.replace("\n", "")
      words.append(line)
  matching_words = []
  if "*" in search_term:
    index = search_term.index("*")
    if index == 0:
      search_term = search_term.replace("*", "")
      for word in words:
        if word.endswith(search_term):
          matching_words.append(word)
    else:
      search_term = search_term.replace("*", "")
      for word in words:
        if word.startswith(search_term):
          matching_words.append(word)
  elif "." in search_term:
    indices_of_dots = []
    for i in range(len(search_term)):
      if search_term[i] != ".":
        indices_of_dots.append(i)
    for word in words:
      if len(word) != len(search_term):
        continue
      matches = 0
      for ii in indices_of_dots:
        if word[ii] == search_term[ii]:
          matches += 1
        if matches == len(indices_of_dots):
          matching_words.append(word)
  else:
    for word in words:
      if search_term == word:
        matching_words.append(word)
  return matching_words
