# song = {
#     "title": "SPB",
#     "Music": ["Hamsaleka", "Arjun Janya"],
#     "songs": [
#         {"Female_Singer": "S.Janaki", "movie": "Ramachari"},
#         {"Female_Singer": "P.Sushila", "Movie": "manedevru"},
#     ],
# }
# print(song.get("songs"))

# # for loop / key:value for key,value in --.items()
# number = dict(first=1, second=2, third=3)
# sq_num = {key: value**2 for key, value in number.items()}
# print(sq_num)
# # to check odd or even value
# x = {num: ("even" if num % 2 == 0 else "Odd") for num in range(1, 10)}
# print(x)

# c = ["CA", "NJ", "RI"]
# t = ["California", "New Jersey", "Rhode Island"]
# answer = {c(i): t(i) for i in range(0, 2)}
# print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)

# alternate soln:
# answer = {thing[0]: thing[1] for thing in person}

check = {count: chr(count) for count in range(65, 91)}
print(check)
