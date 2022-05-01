# This code picks a random food item:
from random import choice

food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])
print(food)

# dictionary
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25,
}
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")


# using get()
# quantity = bakery_stock.get(food)
# if quantity:
#     print("{} left".format(quantity))
# else:
#     print("we don't make that")

# To copy new dictionary
stock_list = {}
stock_list = bakery_stock.copy()

# add new item in the dictionary
stock_list["cheese pizza"] = 5
print(stock_list)
