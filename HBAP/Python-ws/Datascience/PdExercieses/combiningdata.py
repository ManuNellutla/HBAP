import pandas as pd

meet = pd.read_csv("../Datasets/powerliftingmeets.csv")
powerlift = pd.read_csv("../Datasets/openpowerlifting.csv")

left = meet.set_index(['MeetID'])
right = powerlift.set_index(['MeetID'])

print(left.join(right).head(5))
