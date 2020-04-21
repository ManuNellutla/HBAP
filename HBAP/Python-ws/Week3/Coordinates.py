"""
Calculates the distance between two points.
Demonstrates tuples.
"""

from math import sqrt

# Two points
(x1, y1) = (0, 0)
(x2, y2) = (50, 50)

# Calculate distance
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)


p1 = (0, 0)
p2 = (50, 50)

# Calculate distance
distance = sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
print(f"The distance between (0,0) and (50,50) is {distance}")