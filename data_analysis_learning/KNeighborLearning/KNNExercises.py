import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("KNN_Project_Data")

#sb.pairplot(df,hue="TARGET CLASS")
'''
scaling needs to be done as the data in question here is thousands of rows,
nearest neighbour works better with more compact data, to bring in the
wonderers if you will
'''
scaler = StandardScaler()
scaler.fit(df.drop("TARGET CLASS", axis=1))

scaled_features = scaler.transform(df.drop("TARGET CLASS", axis=1))

scaled_df = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print(scaled_df.head())

X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['TARGET CLASS'], test_size=0.30)

#starting of with k=1 and checking what it will yield.
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

pred = knn.predict(X_test)

#Predictions and evaluations, lets check out that model!
from sklearn.metrics import classification_report, confusion_matrix
#checking the matrix and how the confusion matrix balances out.
print(confusion_matrix(y_test, pred))
print()
#check the preditcions for this model
print(classification_report(y_test, pred))
'''
the accuracy could be better (74%) so for this, will build a loop
to see which K value results in lower error rates.
'''
error_rate=[]

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
'''
uncomment the code to see the plot for errors, included as picture also:
plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, marker='o', markerfacecolor='red', markersize=10)
plt.title("Error rate vs K value")
plt.xlabel('K')
plt.ylabel("Error rate")
plt.show()
'''
'''
looks like 16, 23 and 38 k values produce a lower amount of errors. lets
train the model again with 38.
'''
knn = KNeighborsClassifier(n_neighbors=38)
knn.fit(X_train, y_train)

pred = knn.predict(X_test)

print("Trained again with k=38:")
print(confusion_matrix(y_test, pred))
print()
#katsotaan ennustus tarkkuus
print(classification_report(y_test, pred))

'''
Accuracy keeps swaying around 80-88, but significant increase in classification
accuracy. Accuracy increased around 10 points.
'''
#plt.tight_layout()
#plt.show()
