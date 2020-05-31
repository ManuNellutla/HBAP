import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "../../Datasets/Emp_digital_health.csv"

emp_data  = pd.read_csv(filepath)

#sns.distplot(emp_data.Num_Years, label='Years In a role distribution')

# sns.catplot(x='Education Level', y='360_TOT_Avg',data=emp_data, legend_out=True)
# sns.catplot(x='Role_Year', y='360_TOT_Avg',data=emp_data, legend_out=True)
emp_numeric = emp_data._get_numeric_data()
#print(emp_data._get_numeric_data().info())
plot_data= emp_numeric[['360_IA_Score','360_TM_Score','360_IAN_Score','360_CO_Score','360_TOT_Avg']]
# sns.lineplot(x='id', y='360_IA_Score', data=emp_numeric, label='IA Score', linestyle='-')
# sns.lineplot(x='id', y='360_TM_Score', data=emp_numeric, label='TM Score', linestyle='--')
# sns.lineplot(x='id', y='360_IAN_Score', data=emp_numeric, label='IAN Score', linestyle='-.')
# sns.lineplot(x='id', y='360_CO_Score', data=emp_numeric, label='CO Score', linestyle=':')
sns.lineplot(x='id', y='360_TOT_Avg', data=emp_numeric)
plt.ylabel("Score Averages")
plt.ylabel("Employee id")
plt.title("Average score by Emp Id")
#plt.legend(plot_data)
#plt.legend(labels=['l360_IA_Score', '360_TM_Score', '360_IAN_Score','360_TOT_Avg'])
plt.show()



