"""
    i) For each day of the week, randomly generate revenues between $10.00 and $25.00
    ii) Then calculate "Total Revenue for the week" And "Average Revenue for the week day"

"""
# import necessary packages
from calendar import day_abbr
import random
import numpy as np

# place holder for revenue object. I chose dict so i can store revenue per day of the week
revenue = {}

# iterate over the day of the week
for day in day_abbr:
    # add day and randomly generated float value between 10 and 25 to the day index.
    revenue[day] = random.uniform(10.00, 25.00)

#
# for key, value in revenue.items():
#     print(f" Revenue generated on {key} : ${value:.2f}")

print(revenue)

totalRevenue = np.sum(list(revenue.values()))
print(f"\nTotal revenue for the week is : ${totalRevenue:.2f}")
avgRevenue = np.mean(list(revenue.values()))
print(f"Average revenue for the week is : ${avgRevenue:.2f}")
