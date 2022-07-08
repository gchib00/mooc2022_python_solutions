# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

students = {}
exercise_points_per_student = {}
exam_points_per_student = {}

def calc_exercise_points(sum):
  if sum == 40:
    return 10
  if sum < 40 * 0.1:
    return 0
  for i in reversed(range(10)):
    if i == 0 or i == 10:
      continue
    if sum >= 40 * (i / 10):
      return i

def calc_final_points(exercise_points, exam_points):
  total = exercise_points + exam_points
  if total >= 28:
    return 5
  elif total >= 24 and total <= 27:
    return 4
  elif total >= 21 and total <= 23:
    return 3
  elif total >= 18 and total <= 20:
    return 2
  elif total >= 15 and total <= 17:
    return 1
  else:
    return 0

with open(student_info) as file:
  for line in file:
    line = line.strip().split(";")
    if line[0] == "id":
      continue
    students[line[0]] = line[1] + " " + line[2]

with open(exercise_data) as file:
  for line in file:
    line = line.strip().split(";")
    if line[0] == "id":
      continue
    sum = 0
    for i in range(len(line)):
      if i == 0:
        continue
      sum += int(line[i])
    exercise_points_per_student[line[0]] = calc_exercise_points(sum)

with open(exam_data) as file:
  for line in file:
    line = line.strip().split(";")
    if line[0] == "id":
      continue
    sum = 0
    for i in range(len(line)):
      if i == 0:
        continue
      sum += int(line[i])
    exam_points_per_student[line[0]] = sum

for id in students:
  print(students[id], calc_final_points(exercise_points_per_student[id], exam_points_per_student[id]))