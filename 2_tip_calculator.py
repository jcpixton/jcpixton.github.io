print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1
people = int(input("How many people are splitting the bill? "))
tip_amount = (total_bill * tip_percentage) / people
tip_amount = str(round(tip_amount, 2))
print("Each person should pay $" + tip_amount)