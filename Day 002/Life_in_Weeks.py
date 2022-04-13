# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

#     You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


age = input("What is your current age?")

years_left = 90 - int(age)

days = int(years_left) * 365
# each month has 4 weeks
weeks = int(years_left) * 52
# each week has 7 days
months = int(years_left) * 12

print(f"You have {days} days, {weeks} weeks and {months} months left.")
