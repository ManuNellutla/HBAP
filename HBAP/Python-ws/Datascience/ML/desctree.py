from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd


filename = "melb_data.csv"

home_data = pd.read_csv(filename)

home_data = home_data.dropna(axis=0)

y = home_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

x = home_data[melbourne_features]

print(x.describe())

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())

print("The predictions are")
print(melbourne_model.predict(x.head()))

print(y.head())


predicted_home_prices = melbourne_model.predict(x)
mean_error_house_price_predictions = round(mean_absolute_error(y, predicted_home_prices), 2)

print(f"\n The mean error of house prices is ${mean_error_house_price_predictions}")
