from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd


filename = "melb_data.csv"

home_data = pd.read_csv(filename)

home_data = home_data.dropna(axis=0)

y = home_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = home_data[melbourne_features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
