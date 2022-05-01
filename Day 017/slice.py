from readline import insert_text


first_list = [1, 3, 5, 6, 7, 8]
##slice with start
print(first_list[1:])
# gives output with index(1)

# end slice
print(first_list[:3])
# get the index value from 3 to 6
print(first_list[3:6])

## skip by 2 [::2]
print(first_list[1::3])
print(first_list[:1:-1])
##reverse
first_list[::-1]

# insert_text

(first_list[3:]) = "a"
print(first_list)
