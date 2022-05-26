# grocery list

grocery = []
for item in range(1, 10):
    item_list = input("enter the item list :")
    if item_list == "done":
        break
    else:
        grocery.append(item_list)
print("Grocery list is %s" % grocery)


# Check the grocery list

for list in range(1, 10):
    item_check = input("Enter grocery item: ")
    if item_check in grocery:
        print("%s is in the grocery" % item_check)
    elif item_check == "done":
        print("your grocery list is %s" % grocery)
        break
    else:
        print("%s is not in the grocery" % item_check)
        ask = "Do you want to add this item in the grocery list?"
        if ask == "yes":
            grocery.append(item_check)
            print("%s was added to the list" % item_check)
