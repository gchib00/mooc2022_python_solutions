# Write your solution here
attempts = 0
while True:
    attempts += 1
    pin = int(input("PIN:"))
    if pin == 4321:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")