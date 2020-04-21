"""
  Get an input of an item and store in a dictrionary
  Print a list of keys and values, where values are the number of items

"""

inventory = {}

while True:
    item = input("Enter an Item : ")

    if not item:
        break

    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

print("Key     :  Item ")
print("----------------")
for key, value in inventory.items():
    print(f"{key} : {value}")
