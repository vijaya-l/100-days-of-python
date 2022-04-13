# If else condition

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    age = int(input("What is your age?"))
    print("You cab have a ride")
    if age <= 18:
        print("Please pay for the children ticket $ 8")
    else:
        print("Please pay for the adult ticket $ 15")
else:
    print("Sorry!You can't ride the rollercoaster")
