# Write your solution here
contacts = {}
while True:
  inquiry_type = int(input("command (1 search, 2 add, 3 quit):"))
  if inquiry_type == 1:
    searched_name = input("name:")
    if searched_name in contacts:
      for number in contacts[searched_name]:
        print(number)
    else:
      print("no number")
  elif inquiry_type == 2:
    name = input("name:")
    number = input("number:")
    if name in contacts:
      contacts[name].append(number) 
    else:
      contacts[name] = [number]
    print("ok!")
  elif inquiry_type == 3:
    print("quitting...")
    break