# Write your solution here
def summary(dict: dict):
  # Determine averages:
  averages = []
  for student in dict:
    average = get_summary(dict, student)["average"]
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
    num_of_completed = get_summary(dict, student)["total_completed_courses"]
    completed_courses.append((student, num_of_completed))
  highest_completed = 0
  highest_completed_student = ""
  for student in completed_courses:
    if student[1] > highest_completed:
      highest_completed = student[1]
      highest_completed_student = student[0]
  # Print summary
  print("students", len(dict))
  print(f"most courses completed {highest_completed} {highest_completed_student}")
  print(f"best average grade {highest_average} {highest_average_student}")
def add_course(dict: dict, name: str, course: tuple):
  if name in dict:
    dict[name].append(course)     
def print_student(dict: dict, name: str):
  data = get_summary(dict, name)
  if name in dict and data == None:
    print(name+":")
    print(" no completed courses")
  if data != None:
    average = data["average"]
    total_completed_courses = data["total_completed_courses"]
    completed_courses = data["completed_courses"]
    print(name+":")
    print(f" {total_completed_courses} completed courses:")
    for course in completed_courses:
      print(f"  {course[0]} {course[1]}")
    print(" average grade", average)
  else:
    if name not in dict:
      print(f"{name}: no such person in the database")
    else:
      print
def get_summary(dict: dict, name: str):
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
      if len(filtered_courses_list) > 0:
        for course in filtered_courses_list:
          total_score += course[1]
        average = total_score / (len(filtered_courses_list))
        return {
          "average": average,
          "total_completed_courses": len(filtered_courses_list),
          "completed_courses": filtered_courses_list
        }      
    else:
      return None
def add_student(dict: dict, name: str):
  dict[name] = []