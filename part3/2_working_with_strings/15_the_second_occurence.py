# Write your solution here
string = input("Please type in a string:")
sub_string = input("Please type in a substring:")

index = string.find(sub_string) + len(sub_string)
index2 = string[index:].find(sub_string)

if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index2+index}.")