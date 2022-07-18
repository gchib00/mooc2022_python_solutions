# Write your solution here
def read_input(text, num1, num2):
  while True:
    try:
      user_input = int(input(text))
      if user_input > num1 and user_input < num2:
        print("You typed in:", user_input)
        return user_input
      else:
        print(f"You must type in an integer between {num1} and {num2}")
    except ValueError:
      print(f"You must type in an integer between {num1} and {num2}")
      