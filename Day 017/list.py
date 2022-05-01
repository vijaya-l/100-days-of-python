sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

add = ""
for name in sounds:
    print(name.upper())
    add += name.upper()


# using list comprehension
# print("".join([name.upper() for name in sounds]))

# join using comma space
# print(", ".join(sounds))

# print("it's")
# print('"quote"')

##append-its part of one item
sounds.append(["you", "good"])

##extend - it is extend indivisual items
sounds.extend(["music", "melody"])

##insert items in the list

sounds.insert("super", "wow")


# delete the list
sounds.clear()
print(sounds)
