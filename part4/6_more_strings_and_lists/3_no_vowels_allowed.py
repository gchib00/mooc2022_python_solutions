# Write your solution here
def no_vowels(string):
  vowels = ["a", "e", "i", "o", "u"]
  for char in string:
    if char in vowels:
      string = string.replace(char, "")
  return string
if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))