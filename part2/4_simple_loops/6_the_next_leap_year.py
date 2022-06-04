# Write your solution here
year = int(input("Year:"))
nextLeapYear = year
while True:
    nextLeapYear += 1
    if nextLeapYear % 4 == 0:
        if nextLeapYear % 100 == 0 and nextLeapYear % 400 != 0:
            nextLeapYear += 4
            print(f"The next leap year after {year} is {nextLeapYear}")
            break
        else:
            print(f"The next leap year after {year} is {nextLeapYear}")
            break