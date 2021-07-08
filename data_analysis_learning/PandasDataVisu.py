import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
df3 = pd.read_csv('df3')

#Exercise 1
#df3.plot.scatter(x="a", y="b", s=50, c='red', figsize=(12,4))

#Exercise 2
#df3.plot.hist(style='ggplot', bins=30)

#Exercise 4
#df3[['a', 'b']].plot.box()

#Exercise 5
#df3['d'].plot.kde(linestyle='--', linewidth=3)

#Exercise 6
#df3.head(30).plot.area(alpha=0.4)

#Exercise 7
f = plt.figure()
plt.legend(bbox_to_anchor=(1.0, 0.5), loc='center left')
df3.head(30).plot.area(alpha=0.4)

plt.show()
