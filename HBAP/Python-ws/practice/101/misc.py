from datetime import date, timedelta

import math

year = 2012
month = 7
day = 23
birthdate = date(year, month, day)
age = date.today() - birthdate

#print(age.month)
# age = (date.today() - birthdate) // timedelta(days=365.2425)
print(f"Birth date is {birthdate} and the age today is {age} ")

l = [x for x in range(10)]
mean = sum(l)/len(l)
print(mean)
