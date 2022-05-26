# print the tables of entered number
num = input("Enter the number: ")
for i in range(1, 11):
    result = i * int(num)
    print(num, "*", i, "=", result)
