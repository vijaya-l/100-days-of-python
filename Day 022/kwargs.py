def person_fav_color(**kwargs):
    # do not print if name is Pavan
    for person, color in kwargs.items():
        if person != "Pavan":
            print(f"{person}'s favourite color is {color}")


# person_fav_color(Pavan="Green", Vijaya="Red", Reema="Pink", Riya="Blue")
# person_fav_color(Ram="Green", Sita="Red")


def person_fav_color2(**kwargs):
    # do not print if name is Pavan
    # print inside forloop only if Debug key is passed
    report = []
    if "Debug" in kwargs:
        print_in_loop = True
        print("Debug is on, will print inside for loop")
    else:
        print_in_loop = False
    for person, color in kwargs.items():
        if print_in_loop:
            print(person, " ", color)
        if person not in ("Pavan", "Debug"):
            report.append(f"{person}'s favourite color is {color}")
    return report


color_report = person_fav_color2(Pavan="Green", Vijaya="Red", Reema="Pink", Riya="Blue")
print("color report", color_report)


color_report = person_fav_color2(
    Debug="yes", Pavan="Green", Vijaya="Red", Reema="Pink", Riya="Blue"
)
print("color report", color_report)

# write a function add prfix and suffix to word
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


print(combine_words("Rama", prefix="mr"))
print(combine_words("viji", suffix="rao"))
