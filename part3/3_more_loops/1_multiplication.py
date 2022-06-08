# Write your solution here
number = int(input("Pleae type in a number:"))

opr1 = 1
opr2 = 1
while opr1 <= number:
    while opr2 <= number:
        product = opr1 * opr2
        print(f"{opr1} x {opr2} = {product}")
        opr2 += 1 
    opr2 = 1
    opr1 += 1