from random import random

# print(random())


def flip_coins():

    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coins())
