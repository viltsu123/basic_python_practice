import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df911 = pd.read_csv('911.csv')

print(df911.info())
print()
print(df911.head())
print()
print(df911['zip'].value_counts().head(5))
print()
print(df911['twp'].value_counts().head(5))
print()
print(df911['title'].nunique())
print()
columnReason = df911['title'].apply(lambda word: word.split(':')[0])
df911['Reason'] = columnReason
print(columnReason)
print()
print(df911.head(1))
print()
print(df911['Reason'].value_counts())
print()
'''
sb.displot(df911['Reason'], bins=30)
plt.show()
plt.tight_layout()
'''
print(type(df911['timeStamp'].iloc[0]))
print()
print(df911['timeStamp'].iloc[0])
dates = df911['timeStamp'].apply(lambda time: pd.to_datetime(time, errors='coerce'))
df911['timeStamp'] = dates
print()
print(df911['timeStamp'].iloc[0])
print()
print(type(df911['timeStamp'].iloc[0]))
time = df911['timeStamp'].iloc[0]
print(time.hour)
print()

hours = df911['timeStamp'].apply(lambda time: time.hour)
months = df911['timeStamp'].apply(lambda time: time.month)
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
days = df911['timeStamp'].apply(lambda time: time.date().weekday())
def dayofweek(day):
    return dmap[day]

daysWeek = map(dayofweek, days)

df911['Hour'] = hours
df911['Month'] = months
df911['Day of Week'] = list(daysWeek)

#sb.countplot(x=df911['Day of Week'], hue=df911['Reason'])
#sb.countplot(x=df911['Month'], hue=df911['Reason'])
#plt.show()

byMonth = df911.groupby('Month').count()
print(byMonth.head())

#byMonth['twp'].plot()

#sb.lmplot(x='Month',y='twp',data=byMonth.reset_index())
#plt.show()
print()
df911['Date'] = df911['timeStamp'].apply(lambda time: time.date())
#callsDate = df911.groupby('Date').count()
#callsDate['twp'].plot()
#df911[df911['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot()
#plt.title('Traffic')
#plt.show()

#replace Hour with Month to get monthly averages of calls
newdf = df911.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
print(newdf.head())

print()
#day of the week and time where 911 calls cram up
plt.figure(figsize=(12,6))
sb.heatmap(newdf, cmap='viridis')
sb.clustermap(newdf, cmap='viridis')
plt.show()
plt.tight_layout()
