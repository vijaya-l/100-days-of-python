from ast import comprehension
import numbers
from re import X


num = [1, 2, 3, 5, 6]

# for x in num:
#     x *= 5
#     print(x)

# same as above --comprehension
# mul = [x * 5 for x in num]
# print(mul)
numbers = []
numbers = [number * 10 for number in range(0, 10)]
print(numbers)

# To check if codition
even_num = []
even_num = [even for even in range(0, 10) if even % 2 == 0]
print(even_num)


# join
message = ["Hello", "my", "name", "is", "Vijaya"]
name = ["".join(mess for mess in message)]
print(name)
# with space
name = [" ".join(mess for mess in message)]
print(name)
#  without join
let = [mess for mess in message]
print(let[0])
