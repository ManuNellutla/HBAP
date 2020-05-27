import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)
f, ax = plt.subplots(2, 2)
# grouping by country and finding number of reviews
reviews_by_country = reviews.groupby('country').points.count()
ax[0, 0].plot(reviews_by_country, '-ro')
ax[0, 0].set_title("# of Reviews by country")
ax[0, 0].set_ylabel('# of reviews')
ax[0, 0].tick_params('x', labelrotation=45)

# grouping by points and getting average price
avg_price_by_points = reviews.groupby("points").price.mean()
max_price_by_points = reviews.groupby("points").price.max()
print(avg_price_by_points)
print(max_price_by_points)

ax[0, 1].plot(avg_price_by_points, '-g+')
ax[0, 1].set_title("Avg prices by points")
ax[0, 1].set_ylabel('Avg prices')
# ax[0,1].set_xticks(rotation=90)


# review aggregate
country_aggregate = reviews.groupby(['country']).price.agg([len, min, max])
ax[1, 0].plot(country_aggregate['len'], '-b*', country_aggregate['max'], '-r^')
ax[1,1].plot(country_aggregate['max'], '-yo')
plt.show()
