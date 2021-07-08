import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv('Ecommerce Customers')

#exploring data, how does Time on Website correlate to Yearly Amount Spent? sweet spot seems to be around 37 min and spendature is on its highest
#sb.jointplot(x='Time on Website',y='Yearly Amount Spent',data=df)
#plt.show()

#now lets check Time onApp in this same scenario: shorter time produces same or better amounts spent
#sb.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)
#plt.show()

#lets see about length of membership and time on app = tend to be established users who spend 12 minutes or more on the app
#sb.jointplot(x='Time on App',y='Length of Membership',data=df,kind='hex')
#plt.show()

#lets look at the whole data from a plot
#sb.pairplot(df)
#plt.show()

#lets look at a lmplot with yearly amount spent and Length of Membership
#sb.lmplot(x='Yearly Amount Spent',y='Length of Membership',data=df)
#plt.show()
