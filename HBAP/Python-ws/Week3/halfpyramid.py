n= int(input("Enter Pyramid height :"))
res = '#'
for i in range(n):
    for x in range(n-i):
        print(" ", end="")
    print(res)
    res += '#'

