# Write your solution here
limit = int(input("Limit:"))
totalSum = 0
num = 1
performedCalc = "The consecutive sum:"
while totalSum < limit:
    totalSum += num
    if num == 1:
        performedCalc += f" {num}"
    else:
        performedCalc += f" + {num}"
    num += 1
print(f"{performedCalc} = {totalSum}")