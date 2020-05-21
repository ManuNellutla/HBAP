from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd

""" lets setup a method for get MAE """


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    """
    Function to get mean absolute error  value of a model prediction.
    inputs:
       max_leaf_nodes : number of leafs nodes we are modeling on a decision tree
       training values : train_x and train_y
       X and Y values
    output:
        MAE - mean absolute error : Calculated by taking the diff of  predictions - original

    """
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae


def main():
    # file name / path"
    filename = "melb_data.csv"

    """  read data into  data frame """
    home_data = pd.read_csv(filename)

    """ drop nulls or NA """
    home_data = home_data.dropna(axis=0)

    # what will be your Y axis ?
    y = home_data.Price

    # set predictors
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

    # x axis data
    X = home_data[melbourne_features]

    # split data into training and validation data, for both features and target
    # The split is based on a random number generator. Supplying a numeric value to
    # the random_state argument guarantees we get the same split every time we
    # run this script.
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

    help(get_mae)

    maes = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
    # for max_leaf_nodes in [5, 50, 500, 5000]:
    #     my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    #     maes[max_leaf_nodes] = my_mae
    #     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (max_leaf_nodes, my_mae))
    best_candidate = min(maes, key=maes.get)
    print(f"best candidate is {best_candidate}")
    print(f"worse candidate is {max(maes, key=maes.get)}")

    final_model = DecisionTreeRegressor(max_leaf_nodes=best_candidate, random_state=1)

    # fit the final model and uncomment the next two lines
    final_model.fit(X, y)

    final_predictions = final_model.predict(X)

    print(f"\nfinal model predictions :{final_predictions}")


if __name__ == '__main__':
    main()
