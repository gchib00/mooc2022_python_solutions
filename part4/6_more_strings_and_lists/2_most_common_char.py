# Write your solution here
def most_common_character(string):
  arr = []
  for char in string:
    arr.append(string.count(char))
  occurences = max(arr)
  index_of_most_common = arr.index(occurences)
  return string[index_of_most_common]
if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))