# Write your solution here
days = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
weekly = float(input("How much money do you spend on groceries in a week? "))

avgWeekly = weekly + price * days
avgDaily = avgWeekly / 7

print("Average food expenditure:")
print(f"Daily: {avgDaily} euros")
print(f"Weekly: {avgWeekly} euros")