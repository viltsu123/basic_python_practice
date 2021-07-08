import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

#luo excel tyylisen taulukon, näkyy terminaalissa
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print()

#yksittäinen kolumni tieto
print(df['W'])
print()
#lista kolumneja
print(df[['W', 'Z']])
print()
#uuden kolumnin lisääminen, sisältö kahdesta aiemmasta kolumnin riveiltä
df['uusi'] = df['W'] + df['Y']
print(df)
print()

#kolumnin poisto
df.drop('X', axis=1)
print(df)
print()
print('kolumni X ei poistunut, täytyy vielä laittaa inplace arvolle jotta muutos näkyy')
print()
df.drop('X', axis=1, inplace=True)
print(df)
print()

#axis määrää tippuuko rivi vai kolumni
print('rivi tiputus axis=0, kolumni tiputus axis=1')
print()
df.drop('D', axis=0, inplace=True)
print(df)

#valitse rivi, label perusteella, dataframe sisältää Seriessejä (pandas)
print('Valitse A rivi labelilla')
print(df.loc['A'])
print()

#valitse indexin perusteella
print('Valitse A rivi indeksillä')
print(df.iloc[0])
print()

#valitaan yksittäinen solu
print('Yksittäinen solu valinta')
print(df.loc['A','uusi'])
print()

#isompi lohko valinta, ensimmäinen on rivit, toinen kolumnit
print('Valitaan useampi solu')
print(df.loc[['A','B'],['W','uusi']])
print()

#ehdollinen tulostaminen solujen arvoista
print('Katsotaan moni arvo on isompi kuin 0')
print(df>0)
print()

#katsotaan arvot jotka ovat 0 yläpuolelle
print('Arvot vain 0 yläpuolella')
print(df[df>0])
print()

#arvot vain 0 yläpuolella W kolumnissa
print('Tulostetaan rivit joissa W kolumnin arvot isompia kuin 0')
print(df[df['W']>0])
print()

#Haetaan Y kolumni rivit joissa w kolumnin rivien arvo on suurempi kuin 2
print('Haetaan X kolumni jossa w kolumnin arvo on suurempi kuin 2')
print(df[df['W']>2]['Y'])
print()

#useamman ehdon vertailu ja palautus
print('Pidemmän ehdon mukaan tehty palautus, katsotaan W ja Y riviltä ehtoa.')
print(df[(df['W']>0) & (df['Y']>1)])

#indeksi Serien muuttaminen
print()
print('Vaihdetaan labelsia')
print(df)
print('uusi kolumni josta asetetaan indexit')
newindx = 'HEL RAJ KUO KLA'.split()
df['Kunnat'] = newindx
print(df)
print()
df.set_index('Kunnat', inplace=True)
print('uudet labelit:')
print(df)

#multi indexointi, grouppailu
print()
print('multi indeksointi')
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
print()
print('sovelletaan df')
print()
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)

#multiindeksi haku
print()
print('tehdään multiindeksi hakuja:')
print()
print(df.loc['G1'])
print()
print('haetaan ensimmäinen rivi')
print(df.loc['G1'].loc[1])
print()
print('tulostetaan ideille kolumni nimet:')
df.index.names = ['Ryhma', 'Id']
print(df)
print()
print('Haetaan ryhmä G1')
print(df.xs('G1'))
print()
print('haetaan ryhmän G1 rivi 1')
print(df.xs(['G1',1]))
print()
print('haetaan ryhmien ensimmäiset rivit')
print(df.xs(1,level='Id'))
