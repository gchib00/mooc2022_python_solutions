# Write your solution here
def process_dairy_entry():
  entry = input("Diary entry:")
  with open("diary.txt", "a") as file:
    file.write(entry+"\n")
    print("Diary saved")

def read_entries():
  print("Entries:")
  with open("diary.txt") as file:
    for line in file:
      line = line.replace("\n", "")
      print(line)

while True:
  print("1 - add an entry, 2 - read entries, 0 - quit")
  response = input("Function:")
  if response == "1":
    process_dairy_entry()
  elif response == "2":
    read_entries()
  elif response == "0":
    print("Bye now!")
    break