import pandas as pd
import numpy as np

new_data = pd.DataFrame({'Yes': [50, np.nan, np.nan, 40, np.nan, 92], 'No': [33, 22, 4, 21, np.nan, np.nan]})
print(f"new data has nulls \n{new_data.isnull().sum()}")

# new_data = new_data.fillna("0")
# print(f"new data after fillna \n{new_data.isnull().sum()}")

new_data['yes'] = new_data.Yes.replace(np.nan, 'yes')
print(new_data)
