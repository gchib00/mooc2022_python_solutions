# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
students = {}
exercises_per_student = {}

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
    exercises_per_student[line[0]] = sum

for id in students:
  print(students[id], exercises_per_student[id])