import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('Ecommerce Customers')
print(df.columns)

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

#lets get some values into our training model from the dataframe, using the customer related info on x and y is getting yearly amounts
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

#create the variables and instantiate the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
lm = LinearRegression()

#train/fit it in there
lm.fit(X_train, y_train)
print(lm.intercept_)
print()

#lets see about the resulting dataframe
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)

#now lets start predicting of of the data, this is going to be machine guesses of values!
predictions = lm.predict(X_test)

#y_test is going to have real values so lets look at a plot of predictions vs real values! model looks good, correlated results
#sb.scatterplot(x=y_test, y=predictions)
#plt.show()

#now we will evaluate the metrics of real values vs the predictions, got to be honest, these dont tell me that much yet :D i guess the lower the numbers the better the fit,
#and thats what we want for our model :)
print()
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print()

#residual check, what does this tell us?
#sb.histplot(y_test-predictions, kde=True, alpha=0.1, bins=50)
#plt.show()

#we still need to decide, do we focus on web app or phone app development, look at the coefficient dataframe
print(coeff_df)
