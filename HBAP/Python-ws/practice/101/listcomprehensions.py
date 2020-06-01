""" List  comprehension  exercises """

# basic list comprehension with forloop
squares = [n ** 2 for n in range(10)]
print(f"\nsquares from 1 thu 10 : {squares}")

# List comp with if condition
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Print planet names that has more than 5 chars in name
wordyplanets = [planet for  planet in planets if len(planet) > 5]

print(f"\nPlanets with more than 5 chars : {wordyplanets}")


# aggregate functions too like MIN MAX or SUM

nums = [1,4,-5,10,-3,-9,22,34,1]

# how many  negative numbers in the list
numneg = sum([num<0 for num in nums])
print(f"\n There are {numneg} negative  numbers in : {nums}")
# printing total  of negative numbers
totneg = sum([num for num in nums if num<0])
print(f"\n Sum of  negative  numbers in : {nums} is {totneg}")

# any match?
divby7 = any([num %  11== 0 for num in nums])
print(f"\n  {nums} has any number divisibile  by 7 is {divby7}")