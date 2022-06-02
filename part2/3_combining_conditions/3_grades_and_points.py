# Write your solution here
grade = int(input("How many points [0-100]:"))

if grade > 100 or grade < 0:
    print("Grade: impossible!")
elif grade >= 90:
    print("Grade: 5")
elif grade >= 80:
    print("Grade: 4")
elif grade >= 70:
    print("Grade: 3")
elif grade >= 60:
    print("Grade: 2")
elif grade >= 50:
    print("Grade: 1")
else:
    print("Grade: fail!")