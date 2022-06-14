# Write your solution here
def palindromes(word: str):
  if word == word[::-1]:
    print(f"{word} is a palindrome!")
    return True
  print("that wasn't a palindrome")
  return False

while True:
  word = input("Please type in a palindrome: ")
  response = palindromes(word)
  if response == True:
    break