# Write your solution here
from random import randint
from string import ascii_lowercase

def generate_password(passLength: int):
  password = ""
  for i in range(passLength):
    letter = ascii_lowercase[randint(0, passLength)]
    password += letter
  return password

if __name__ == "__main__":
  for i in range(10):
      print(generate_password(8))