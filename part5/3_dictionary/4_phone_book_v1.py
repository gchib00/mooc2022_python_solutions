# Write your solution here
contacts = {}
while True:
  inquiry_type = int(input("command (1 search, 2 add, 3 quit):"))
  if inquiry_type == 1:
    searched_name = input("name:")
    if searched_name in contacts:
      print(contacts[searched_name])
    else:
      print("no number")
  elif inquiry_type == 2:
    name = input("name:")
    number = input("number:")
    contacts[name] = number
    print("ok!")
  elif inquiry_type == 3:
    print("quitting...")
    break