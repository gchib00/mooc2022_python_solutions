# Write your solution here
from datetime import datetime

day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))

millenium = datetime(2000, 1, 1)
difference = millenium - datetime(year, month, day)

if difference.days - 1 < 0:
  print("You weren't born yet on the eve of the new millennium.")
else:
  print(f"You were {difference.days - 1} days old on the eve of the new millennium.")