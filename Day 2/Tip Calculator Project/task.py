print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount = bill*(tip/100)
print(tip_amount)
total_bill = bill + tip_amount
print(total_bill)
each_pay = total_bill/ people
final_amount = round(each_pay, 2)
print(f"Each person should pay: ${final_amount}")

