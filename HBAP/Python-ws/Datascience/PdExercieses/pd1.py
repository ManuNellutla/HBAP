import pandas as pd

# creating a data frame

df = pd.DataFrame({'Yes': [50, 121, 30, 40], 'No': [33, 22, 4, 21]})

df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                    'Sue': ['Pretty good.', 'Bland.']},
                   index=['Product A', 'Product B'])

print(df)

print(df2)

df2.to_csv("cows_and_goats.csv")
