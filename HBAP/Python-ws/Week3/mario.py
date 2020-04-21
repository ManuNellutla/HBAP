# get user input between 1 and 4
x = int(input("Enter a number between 1 and 4 : "))

errCount = 0

# validate if value is between 1 and 4
while x < 1 or x > 4:
    # Looks like user doesn't follow rules. count errors
    errCount += 1

    # print error message
    print(f"!!Error ({errCount}) !! : Number is not between 1 and 4. Please retry. ")

    # re ask for input
    x = int(input("Enter a number between 1 and 4 :"))

# Loop input number of times
for a in range(0, x):
    # print vertical block
    print("#")

# print new line.
print("\n")
