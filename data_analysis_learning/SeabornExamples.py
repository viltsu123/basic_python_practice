import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.displot(tips['total_bill'], kde=True, bins=30)

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

sns.pairplot(tips, hue='sex', palette='coolwarm')

plt.show()
