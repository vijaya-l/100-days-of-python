#  Create a list called instructors
instructors = []
# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.extend(["colt", "blue", "lisa"])
print(f"list{instructors}")
# Remove the last value in the list
# instructors.remove("Lisa")
# print(instructors)
# # Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")

# modify the first letter as capital letter
instructors[0].capitalize()
# instructors[2].lower()
print(instructors)
