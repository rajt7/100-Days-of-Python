print("Welcome to the tip calculator.")

bill = float(input("What is your total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10,12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill * (tip_percentage / 100))
pay_per_person = bill_with_tip / no_of_people

print("Each person should pay: $%.2f" % pay_per_person)
