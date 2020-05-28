import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mafs = pd.read_csv("../../Datasets/titanic_test.csv")

print(mafs.info())

# Set the width and height of the figure
plt.figure(figsize=(16, 6))

# # get numeric data undocumented  method
# numeric_data = power_lifting_data._get_numeric_data()
# print(f"  \n after getnumeric\n {numeric_data.info()}")
#
plotdata = mafs[['PassengerId', 'Pclass', 'Fare']]
sns.lineplot(data=plotdata)

plt.show()
