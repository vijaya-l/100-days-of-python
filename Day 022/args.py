def fullname(*args):
    full_name = ""
    for name_part in args:
        full_name = full_name + " " + name_part
    # Trim the space before returning
    return full_name.strip()


print(fullname("Viji", "Rao", "Nanjangud"))

print(fullname("Viji", "Rao"))

print(fullname("Toby"))

print(fullname("name1", "name2", "name3", "name4"))

print(fullname())

# 2.
def contains_purple(*args):
    if "purple" in args:
        return True
    return False


print(contains_purple("purple"))

print(contains_purple("red", "purple"))

print(contains_purple())

print(contains_purple("green"))


# 3.adding multiple arguments


def add_all(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add_all(5, 6, 8))
print(add_all(10))
print(add_all(10, 10, 10, 10))

# sequences

# good
# for item in sequence:
#     use the item

# bad
# for i in range(len(sequence)):
#    use sequence[i]
#
