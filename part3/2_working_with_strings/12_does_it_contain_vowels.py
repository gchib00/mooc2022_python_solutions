# Write your solution here
string = input("Please type in a string:")
a = "a not found"
e = "e not found"
o = "o not found"
if "a" in string:
    a = "a found"
if "e" in string:
    e = "e found"
if "o" in string:
    o = "o found"
print(a)
print(e)
print(o)