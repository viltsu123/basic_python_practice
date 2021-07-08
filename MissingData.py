import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
                    'B':[5,np.nan,np.nan],
                    'C':[1,2,3]})
print('Puuttuva data taulukko')
print(df)
print()
print('poistetaan puuttuvat arvot')
print(df.dropna())
print()
print('poistetaan puuttuvat arvot kolumneittain')
print(df.dropna(axis=1))
print()
print('poistetaan rivit joissa vähintään 2 nannia')
print(df.dropna(thresh=2))
print()
print('täytetään soluja arvolla FILLERI ARVO')
print(df.fillna(value='FILLERI ARVO'))
print()
print('Täytetään kolumnin A soluja joissa nan kolumnin rivien keskiarvolla')
print(df['A'].fillna(value=df['A'].mean()))
