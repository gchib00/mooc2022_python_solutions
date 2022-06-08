# Write your solution here
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        factorial = 1
        helper_num = 1
        while helper_num < number:
            helper_num += 1
            factorial *= helper_num
        print(f"The factorial of the number {number} is {factorial}")
