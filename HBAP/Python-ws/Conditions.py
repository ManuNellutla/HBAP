# Conditional programing

x = int(input("Enter Fiscal Revenue: "))
y = int(input("Enter Operating Costs: "))

if x > y:
    print(f"We have profits of {x-y}")
elif x == y:
    print(f"We broke even")
else :
    print(f"We have a loss : {x-y}")

