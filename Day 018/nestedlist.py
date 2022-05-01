# nested_list = [[num for num in range(1, 4)] for val in range(1, 4)]
# print(nested_list)


# pattern = [
#     ["x" if num % 2 != 0 else "o" for num in range(1, 4)] for list in range(1, 4)
# ]
# print(pattern)

answer = [[x for x in range(0, 10)] for val in range(1, 9)]
print(answer)
