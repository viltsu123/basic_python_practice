'''
The assignment for this part of data analysis read as follows:
Lending Club connects people who need money (borrowers) with
people who have money (investors).
Hopefully, as an investor you would want to invest
in people who showed a profile of having a high
probability of paying you back. We will try to create a
model that will help predict this.

the idea is to present a model that have paid their loans on time
for possible investors.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

#look at the data
loans = pd.read_csv("loan_data.csv")
'''
print(df.info())
print()
print(df.head())
print()
print(df.describe())
'''
#explore the data
#plt.figure(figsize=(10,6))

'''
#create two histograms on top of each other based on credit.policy value
loans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='Credit.Policy=1')
loans[loans['credit.policy']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='Credit.Policy=0')

#looking at not.fully.paid column
loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.5, color='blue', bins=30, label='not.fully.paid=1')
loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red', bins=30, label='not.fully.paid=0')

plt.legend()
plt.xlabel('FICO')
'''
'''
#lets see loan purposes and what has been paid off fully
sb.countplot(data=loans, hue='not.fully.paid', x='purpose')
'''
'''
#next looking at fico score and interest rate
sb.jointplot(x="fico", y="int.rate", data=loans, color="purple")
#looks like the higher the fico score is the lower the interest rate goes
'''
'''
#and finally check to see fully paid values againsta fico and in rate
sb.lmplot(data=loans, x="fico", y="int.rate", hue="credit.policy", col="not.fully.paid")
#looks like the people that were qualified by the lending company and did
#pay the loans back in full had generally higher fico scores
'''
#plt.show()
print(loans.info())

cat_feats = ["purpose"]
#unpack the categorical data to numerical columns
final_data=pd.get_dummies(loans, columns=cat_feats, drop_first=True)
print(final_data.info())
print(final_data.head(1))

X_train, X_test, y_train, y_test = train_test_split(final_data.drop("not.fully.paid", axis=1), final_data["not.fully.paid"], test_size=0.3)
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

prediction = dtree.predict(X_test)
print(classification_report(y_test, prediction))
print()
print(confusion_matrix(y_test, prediction))

#lets get the same with random forest classifier

rndtree = RandomForestClassifier()
rndtree.fit(X_train,y_train)
predictionrnd = rndtree.predict(X_test)

print(classification_report(y_test, predictionrnd))
print()
print(confusion_matrix(y_test, predictionrnd))

#the decision tree classifier did better based on the confusion matrix results
#both predicted over or under the results but random forest was way off
#with the not fully paid predictions, and also with f1-scores and recall accuracy.
