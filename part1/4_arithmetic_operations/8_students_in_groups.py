# Write your solution here
studentsNum = int(input("How many students on the course?"))
groupSize = int(input("Desired group size?"))

groupsNum = studentsNum//groupSize

if (studentsNum % groupSize > 0):
    groupsNum += 1

print(f"Number of groups formed: {groupsNum}")