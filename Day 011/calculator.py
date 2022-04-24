logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)


# Adding 2 numbers
def add(n1, n2):
    return n1 + n2


# # Subtract 2 numbers
def sub(n1, n2):
    return n1 - n2


# # multiply 2 numbers
def mul(n1, n2):
    return n1 * n2


# Devide 2 numbers
def div(n1, n2):
    return n1 / n2


calculator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

num1 = float(input("enter first number: "))

for operation in calculator:
    print(operation)
operation_symbol = input("pick the operaion symbol from the above list")
calc = calculator[operation_symbol]

num2 = float(input("enter 2nd number: "))

answer = calc(num1, num2)
# print(answer)
print(f"{num1}{operation_symbol}{num2}={answer}")
