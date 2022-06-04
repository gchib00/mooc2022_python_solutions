# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
posCount = 0
negCount= 0
totalSum = 0
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    else:
        totalSum += num
        if num > 0:
            posCount += 1
        else:
            negCount += 1
totalCount = negCount+posCount
print("Positive numbers ", posCount)
print("Negative numbers ", negCount)
print("Numbers typed in", totalCount)
print("The sum of the numbers is", totalSum)
print("The mean of the numbers is", totalSum/totalCount)