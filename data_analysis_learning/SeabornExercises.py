import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

#Exercise1
#sns.jointplot(x="fare", y="age", data=titanic, kind="scatter")

#Exercise 2
#sns.displot(titanic['fare'])

#Exercise 3
#sns.boxplot(x="class",y="age",data=titanic,palette="rainbow")

#Exercise4
#sns.swarmplot(x="class", y="age", data=titanic)

#Exercise5
#sns.countplot(x="sex",data=titanic)

#Exercise 6
#sns.heatmap(titanic.corr(),cmap='coolwarm', vmax=1, center=0, vmin=-1)

#Exercise 7
#g = sns.FacetGrid(titanic, col="sex")
#g.map(plt.hist, 'age')

plt.tight_layout()
plt.show()
