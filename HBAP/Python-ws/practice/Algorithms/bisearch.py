# Python3 program to implement Binary
# Search for strings

# Returns index of x if it is present
# in arr[], else return -1
def find(L, target):
    start = 0
    end = len(L) - 1
    it = 0
    while start <= end:
        middle = int((start + end)/ 2)
        midpoint = L[middle]
        it += 1
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            print(f"match found at position {middle+1} and after {it} iterations")
            return midpoint


# Driver Code
if __name__ == "__main__":

    arr = ["afternoon", "offer", "beside",
           "nation", "mountain", "alphabet", "pleasant",
           "reach", "possible", "sick", "produce", "rich", "stiller", "stoney"]
    arr = sorted(arr)
    print(f"sorted array {arr}")
    x = input("Pick a string from above list : ")
    result = find(arr, x)

    if result == -1:
        print("Element not present")
    else:
        print("Element found at index",
              result)

