import time
from random import randint

for i in range(1, 85):
    print("")

space = ""

for i in range(1, 500):
    count = randint(1, 100)
    while count > 0:
        space += " "
        count -= 1
    if i % 10 == 0:
        print(space + "πHappy Birthday!")
    elif i % 9 == 0:
        print(space + "π")
    elif i % 5 == 0:
        print(space + "π")
    elif i % 4 == 0:
        print(space + "π my dear Husbandπ")
    elif i % 8 == 0:
        print(space + "π")
    elif i % 7 == 0:
        print(space + "π«")
    elif i % 6 == 0:
        print(space + "Happy Birthday!π")
    else:
        print(space + "πΈ")

    space = ""
    time.sleep(0.2)
