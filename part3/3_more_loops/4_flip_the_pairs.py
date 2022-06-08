# Write your solution here
num = int(input("Please type in a number:"))
helper_num = 1
while helper_num <= num:
    if helper_num % 2 != 0 and helper_num + 1 <= num:
        print(helper_num + 1)
    elif helper_num % 2 == 0:
        print(helper_num - 1)
    else:
        print(helper_num)
    helper_num += 1