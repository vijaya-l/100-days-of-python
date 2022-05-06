def count_sevens(*args):
    return args.count(7)


nums = [
    90,
    1,
    35,
    67,
    89,
    20,
    3,
    1,
    2,
    3,
    4,
    5,
    6,
    9,
    34,
    46,
    57,
    68,
    79,
    7,
    23,
    34,
]

print(count_sevens(*nums))


# 2.unpack dictionary
def name(first, last):
    print(f"{first} says hello to {last} ")


full_name = {"first": "vijaya", "last": "pavan"}
name(**full_name)
