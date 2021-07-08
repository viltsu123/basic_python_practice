import plotly.graph_objs as go
from plotly.offline import iplot
import pandas as pd

#Exercise 1
'''
df2014 = pd.read_csv('2014_World_Power_Consumption')

data = dict(type = 'choropleth',
            locations = df2014['Country'],
            locationmode = 'country names',
            colorscale = 'Earth',
            text = df2014['Text'],
            z = df2014['Power Consumption KWH'],
            colorbar = {'title':'Power Consumption 2014'})

layout = dict(title = '2014 Global Power Consumption',
                geo = dict(showframe = False,
                            projection = {'type':'mercator'}))
'''

#Exercise 2

dfElection = pd.read_csv('2012_Election_Data')

data = dict(type = 'choropleth',
            locations = dfElection['State Abv'],
            locationmode = 'USA-states',
            colorscale = 'Portland',
            text = dfElection['State'],
            z = dfElection['Voting-Age Population (VAP)'])

layout = dict(title = '2012 VAP Population',
                geo = dict(scope = 'north america',
                            projection = {'type':'mercator'}))

choromap = go.Figure(data=[data], layout=layout)
iplot(choromap, validate=False)
