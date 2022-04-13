# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Example Input

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# # Example Output

# Each person should pay: $19.93


bill = input("What was the total bill?\n")
tip = input("what is the tip\n")
persent_tip = (float(tip) / 100) * float(bill)
final_bill = float(bill) + persent_tip

print("added tip to bill\n" + str(final_bill))

people = input("number of people\n")
per_final_bill = final_bill / float(people)

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60
per_final_bill = "{:.3f}".format(per_final_bill)
print(f"Each person should pay: ${per_final_bill}")
