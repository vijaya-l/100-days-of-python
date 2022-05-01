introduce = {"name": "Vijaya", "age": 30, "Contry": "India", "favourite": "cook"}
# join = "{} {}".format(introduce["name"], introduce["Contry"])

# # use.values() for key/use.keys() for keys/use.items() for both
# print(introduce.keys())

# DON'T TOUCH PLEASE!
donations = dict(
    sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0
)
# DON'T TOUCH PLEASE!
total_donations = 0

for x in donations.values():
    total_donations += x
# print(total_donations)
# print(type(total_donations))

# To copy introduce into hello .copy()
hello = introduce.copy()

# To empty the dictionary use .clear()
# hello.clear()
# print(hello)

# To create key value from comma seperated value

print({}.fromkeys(["email"], "reachviji@gmail.com"))
print({}.fromkeys("email", "reachviji@.com"))
print({}.fromkeys(["a"], [1, 2, 4, 5]))

# To get key -value
print(introduce.get("name"))

# To set all keys value as 0
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements",
]
initial_game_state = dict.fromkeys(game_properties, 0)

# To pop / remove item
initial_game_state.pop("number_of_lives")


# To popitem/ randomly removed

initial_game_state.popitem()
print(initial_game_state)
