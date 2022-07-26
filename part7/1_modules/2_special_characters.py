# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
  stringLtrs = list(my_string)
  ascii_letters_list = []
  punctuation_list = []
  remaining_list = []
  for ltr in stringLtrs:
    if ltr in ascii_letters:
      ascii_letters_list.append(ltr)
    elif ltr in punctuation:
      punctuation_list.append(ltr)
    else:
      remaining_list.append(ltr)
  return (
    "".join(ascii_letters_list),
    "".join(punctuation_list),
    "".join(remaining_list)
  )