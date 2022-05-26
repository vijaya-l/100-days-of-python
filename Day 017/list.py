import numbers


sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

add = ""
for name in sounds:
    print(name.upper())
    add += name.upper()

# using list comprehension
# print("".join([name.upper() for name in sounds]))

# 'join' using comma space
print(", ".join(sounds))

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

# delete items with index /pop()-last item,pop(0)-first item
sounds.pop()
sounds.pop(2)

# remove
sounds.remove("wow")

##index
# numbers=[1,2,4,6,6]
# numbers.index(2)--> 1

##sort-- sorting list
sounds.sort()

# dir - list of operations
print(dir(sounds))
