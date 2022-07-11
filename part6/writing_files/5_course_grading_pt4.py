# tee ratkaisu tänne
# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_data = input("Course information: ")
students = {}
course_info = {}

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

with open(course_data) as file:
  for line in file:
    line = line.replace("\n", "")
    line = line.split(": ")
    if line[0] == "name":
      course_info["name"] = line[1]
    elif line[0] == "study credits":
      course_info["credits"] = line[1]

with open(student_info) as file:
  for line in file:
    line = line.strip().split(";")
    if line[0] == "id":
      continue
    students[line[0]] = {
      "name": line[1] + " " + line[2]
    }

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
    students[line[0]]["exec_nbr"] = sum
    students[line[0]]["exec_pts."] = calc_exercise_points(sum)

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
    students[line[0]]["exm_pts."] = sum

def calc_final_points(student_id):
  total = students[student_id]["exm_pts."] + students[student_id]["exec_pts."]
  students[student_id]["tot_pts."] = total
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

for student_id in students:
  students[student_id]["grade"] = calc_final_points(student_id)

# def write_to_csv():
name = "name"
exec_nbr = "exec_nbr"
exec_pts = "exec_pts."
exm_pts = "exm_pts."
tot_pts = "tot_pts."
grade = "grade"

txt_target_file = "results.txt"
csv_target_file = "results.csv"

def write_to_txt():
  with open("results.txt", "w") as file:
    file.write(f"{course_info['name']}, {course_info['credits']} credits\n")
    file.write("="*38+"\n")
    file.write(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade:10}\n")
    for id in students:
      file.write(f"{students[id][name]:30}{students[id][exec_nbr]:<10}{students[id][exec_pts]:<10}{students[id][exm_pts]:<10}{students[id][tot_pts]:<10}{students[id][grade]:<10}\n")

def write_to_csv():
  with open("results.csv", "w") as file:
    for id in students:
      file.write(f"{id};{students[id][name]};{students[id][grade]}\n")

write_to_txt()
write_to_csv()
print(f"Results written to files {txt_target_file} and {csv_target_file}")