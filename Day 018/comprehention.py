# ------if condition--------
# 1.multipy by 12 in range 1 to 100
# answer = [answer * 12 for answer in range(1, 100)]

# 2.for all the numbers between 1 and 100 divisible by 12
# answer = [val for val in range(1, 101) if val % 12 == 0]
# print(answer)

# 3.get the message without vowels
answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)
