# Write your solution here
limit = int(input("Limit:"))
totalSum = 0
num = 1
while totalSum < limit:
    totalSum += num
    num += 1
print(totalSum)