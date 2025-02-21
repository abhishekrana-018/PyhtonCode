# Greeting message
print("Welcome to the Tip Calculator")

# Ask for the total Bill
bill = float(input("What is the your total bill. $"))

# Ask for how much tip they want to give
tip = float(input("How much tip you wnat to give? $10, $12 or $15? $"))

# How many people they want to split the bill
no_of_people = int(input("How many people to split the bill?"))

# Calculate how much each should pay
pay = ((bill+tip)/no_of_people)

print(f"Each person should pay: ${round(pay,2)}")