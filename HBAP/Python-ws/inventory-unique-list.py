"""
 get a unique item list from a pre-existing list
 and sort them
"""

items =["bread", "butter",  "milk", "bread", "buscuits", "butter"]

print(f"Unaltered list : {items}")

# print unique and sort items on the fly
print(f"Unique and sorted : {sorted(set(items))}")

