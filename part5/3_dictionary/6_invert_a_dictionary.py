# Write your solution here
def invert(dict):
  inverted_dict = {}
  for item in dict:
    key_val = dict[item]
    inverted_dict[key_val] = item
  dict.clear()
  for item in inverted_dict:
    key_val = inverted_dict[item]
    dict[item] = key_val