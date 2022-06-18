# Write your solution here
def ask_for_data():
  data = []
  while True:
    line = input("Exam points and exercises completed:")
    if len(line) == 0:
      break
    data.append(line)
  return data

def convert_to_exercise_points(completed_exercises):
  completed_exercises = int(completed_exercises)
  if completed_exercises == 100:
    return 10
  elif completed_exercises < 10:
    return 0
  else:
    return int(str(completed_exercises)[:1])

def get_a_course_grade(course_data):
  course_data = course_data.split()
  total_points = int(course_data[0]) + convert_to_exercise_points(course_data[1])
  if int(course_data[0]) < 10 or total_points <= 14:
    return 0
  elif total_points <= 17:
    return 1
  elif total_points <= 20:
    return 2
  elif total_points <= 23:
    return 3
  elif total_points <= 27:
    return 4
  elif total_points <= 30:
    return 5

def get_average(data):
  total_points = 0
  for course_data in data:
    course_data = course_data.split()
    total_points += int(course_data[0]) + convert_to_exercise_points(course_data[1])
  return total_points / len(data)

def get_pass_rate(course_grades):
  failed = 0
  for grade in course_grades:
    if grade == 0:
      failed += 1
  if failed == 0:
    return 100
  return 100 - (100 / (len(course_grades) / failed))  

def print_stats(data, course_grades):
  print("Statistics:")
  print(f"Points average: {get_average(data):.1f}")
  print(f"Pass percentage: {get_pass_rate(course_grades):.1f}")
  print("Grade distribution:")
  index = 5
  while index >= 0:
    matching_items = 0
    for grade in course_grades:
      if grade == index:
        matching_items += 1
    if matching_items > 0:
      stars = matching_items * "*"
      print(f"{index}: {stars}")
    else:
      print(f"{index}:")
    index -= 1

def main():
  data = ask_for_data()
  course_grades = []
  for course_data in data:
    course_grades.append(get_a_course_grade(course_data))
  print_stats(data, course_grades)

main()