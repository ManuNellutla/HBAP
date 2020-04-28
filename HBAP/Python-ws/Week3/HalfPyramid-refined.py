"""
Print a right justified pyramid of HASHES based on user input of height

"""
# Ask for user input on height and add one so that we can actually get that height.
ht = int(input("Enter pyramid height between 3 and 10 : ")) +1

# check if the input is out of desired limit and do it until they get it right
while ht < 3 or ht > 10:
    # re-prompt for valid input
    ht = int(input("Error ! Enter valid pyramid  height between 3 and 10 : ")) +1

# loop till user desired times (ht +1) to get ht number of hashes..
for i in range(1, ht):
    # Characters are internally represented as int values.
    # so they can be multiplied.
    # height - i times the 'blanks' and i times ' hash ' value
    print(' '*(ht-i -1), '#'*i)


