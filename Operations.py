import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())
print()
print('Operations esimerkkejä')
print()

print('Uniikit arvot col2')
print()
print(df['col2'].unique())
print('uniikit lukumäärä col2sessa')
print()
print(df['col2'].nunique())
print()
print('arvojen määrä col2')
print(df['col2'].value_counts())
print()

print('Selecting Data')
print()
#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)
print()
print('Apply functions')
print()
def times2(x):
    return x*2

print(df['col2'].apply(times2))
print()
print(df['col3'].apply(len))
print()
print(df['col1'].sum())
print()
print('permanent removal of column')
del df['col1']
print(df)
print()
print(df.columns)
print(df.index)
print(df)
print()
print('Sorttaus')
print(df.sort_values(by='col2'))
print()
print('null tarkistus arvoille')
print(df.isnull())
print()
print('Pivot table kummallisuus')
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))
