# Write your solution here
def summary(dict: dict):
  # Determine averages:
  averages = []
  for student in dict:
    average = print_student(dict, student)[0]
    averages.append((student, average))
  highest_average = 0
  highest_average_student = ""
  for student in averages:
    if student[1] > highest_average:
      highest_average = student[1]
      highest_average_student = student[0]
  # Determine completed courses:
  completed_courses = []
  for student in dict:
    num_of_completed = print_student(dict, student)[1]
    completed_courses.append((student, num_of_completed))
  highest_completed = 0
  highest_completed_student = ""
  for student in completed_courses:
    if student[1] > highest_completed:
      highest_completed = student[1]
      highest_completed_student = student[0]
  # Print summary
  print(f"most courses completed {highest_completed} {highest_completed_student}")
  print(f"best average grade {highest_average} {highest_average_student}")
def add_course(dict: dict, name: str, course: tuple):
  if name in dict:
    dict[name].append(course)     
def print_student(dict: dict, name: str):
  if name in dict:
    filtered_courses_list = []
    total_score = 0
    for course in dict[name]:
      if course[1] > 0:
        matches = 0
        for filtered_course in filtered_courses_list:
          if course[0] == filtered_course[0]:
            if course[1] > filtered_course[1]:
              filtered_courses_list.remove(filtered_course)
              filtered_courses_list.append(course)
            matches += 1
        if matches == 0:
          filtered_courses_list.append(course)
    print(name+":")
    if len(filtered_courses_list) == 0:
      print(" no completed courses")
    else:
      print(f" {len(filtered_courses_list)} completed courses:")
      for course in filtered_courses_list:
        print(f"  {course[0]} {course[1]}")
        total_score += course[1]
      average = total_score / (len(filtered_courses_list))
      print(" average grade", average)
      return (average, len(filtered_courses_list))
  else:
    print(f"{name}: no such person in the database")  
def add_student(dict: dict, name: str):
  dict[name] = []

if __name__ == "__main__":
  students = {}
  add_student(students, "Peter")
  add_course(students, "Peter", ("Software Development Methods", 5))
  summary(students)
