# Write your solution here
from random import randint
from string import ascii_lowercase

def generate_password(passLength: int):
  password = ""
  for i in range(passLength):
    letter = ascii_lowercase[randint(0, passLength)]
    password += letter
  return password

def generate_strong_password(passLength, numChar, specialChar):
  specialChars = ["!","?","=","+","-","(",")","#"]
  password = ""
  # Step 1 - generate random string
  for i in range(passLength):
    letter = ascii_lowercase[randint(1, passLength)]
    password += letter
  if numChar == True:
    # Step 2 - inject random amount of numChars inside the string
    amount_of_chars_to_replace = randint(1, passLength-1)
    for i in range(amount_of_chars_to_replace):
      password = list(password)
      password[randint(0, passLength-1)] = str(randint(0, 9))
      password = "".join(password)      
  if specialChar == True:
    # Step 3 - inject random amount of specialChars inside the string
    amount_of_chars_to_replace = randint(1, passLength-1)
    for i in range(amount_of_chars_to_replace):
      password = list(password)
      password[randint(0, passLength-1)] = specialChars[(randint(0, len(specialChars)-1))]
      password = "".join(password)
  return password
if __name__ == "__main__":
  for i in range(10):
    print(generate_strong_password(16, True, False))
