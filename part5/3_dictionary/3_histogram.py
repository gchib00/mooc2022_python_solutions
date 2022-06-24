# Write your solution here
def histogram(string):
  grouped_chars = {}
  for char in string:
    if char in grouped_chars:
      grouped_chars[char] += 1
    elif char not in grouped_chars:
      grouped_chars[char] = 1
  # Print result:
  for group in grouped_chars:
    print(group, grouped_chars[group] * '*')
if __name__ == "__main__":
  histogram("abba")
  histogram("statistically")