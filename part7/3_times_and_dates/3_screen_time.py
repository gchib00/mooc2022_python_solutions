from datetime import datetime, timedelta

file_name = input("Filename: ")
starting_date = input("Starting date: ")
starting_date = datetime.strptime(starting_date, "%d.%m.%Y")
days_len = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

counter = 0
spent_time = []
total_minutes = 0
new_date = starting_date
while counter < days_len:
  if counter != 0:
    new_date += timedelta(days=1)
  times = input(f"Screen time {new_date.strftime('%d.%m.%Y')}: ")
  times = times.split(" ")
  for time in times:
    total_minutes += int(time)
  day = {
    "tv": int(times[0]),
    "computer": int(times[1]),
    "mobile": int(times[2]),
    "date": new_date.strftime('%d.%m.%Y')
  }
  spent_time.append(day)
  counter += 1

with open(file_name, "w") as file:
  print(spent_time[-1])
  time_period = starting_date.strftime('%d.%m.%Y') + "-" + spent_time[-1]["date"]
  average_minutes = (total_minutes / len(spent_time))
  
  file.write("Time period: " + time_period + "\n")
  file.write("Total minutes: " + str(total_minutes) + "\n")
  file.write("Average minutes: " + str(average_minutes) + "\n")

  for day in spent_time:
    minutes = str(day["tv"]) + "/" + str(day["computer"]) + "/" + str(day["mobile"])
    file.write(day["date"] + ": " + minutes + "\n")

print(f"Data stored in file {file_name}")