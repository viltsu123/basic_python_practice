import numpy as np
import pandas as pd

print('csv input')
print()
df = pd.read_csv('example.csv')
print(df)
print()
print('csv output')
print()
df.to_csv('example', index=False)

print('excel input, lukee vain dataa, jos macroja voi excel funkkari kaatua')
print()
exdf = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1', header=1)
print(exdf)
print()
print('excel out')
print()
exdf.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
print()
print('html data read')
print()

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0])
