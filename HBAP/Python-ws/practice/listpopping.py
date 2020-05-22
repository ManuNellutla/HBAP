planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for i in range(len(planets)):
    print(planets)
    # remove  last one.
    planets.pop()

pyramid = list("############")

for c in range(len(pyramid)):
    print(pyramid)
    pyramid.pop()

pyramid = "whatascrewup"
for char in pyramid:
    s = ""
    print(s.join(pyramid))
    pyramid[c] = " "
