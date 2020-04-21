"""
 playing with main method
"""
import random
import numpy as np

def main():
    totRev = getTotalRevenue()
    print(f" total revenue is ${totRev:.2f}")


def getTotalRevenue():
    rev = []
    for i in range(0, 10):
        rev.append(random.uniform(10, 20))
    return np.sum(rev)


if __name__ == "__main__":
    # execute only if run as a script
    main()
