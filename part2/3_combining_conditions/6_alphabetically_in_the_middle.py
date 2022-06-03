# Write your solution here
ltr1 = input("1st letter:")
ltr2 = input("2nd letter:")
ltr3 = input("3rd letter:")

if ltr1 > ltr2 and ltr1 > ltr3:
    if ltr2 > ltr3:
        print("The letter in the middle is", ltr2)
    else:
        print("The letter in the middle is", ltr3)
elif ltr2 > ltr1 and ltr2 > ltr3:
    if ltr1 > ltr3:
        print("The letter in the middle is", ltr1)
    else:
        print("The letter in the middle is", ltr3)
else:
    if ltr1 > ltr2:
        print("The letter in the middle is", ltr1)
    else:
        print("The letter in the middle is", ltr2)