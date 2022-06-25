# Write your solution here
def create_tuple(n1, n2, n3):
  greatest = max([n1, n2, n3])
  smallest = min([n1, n2, n3])
  numbers_sum = sum([n1, n2, n3])
  return (smallest, greatest, numbers_sum)
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))