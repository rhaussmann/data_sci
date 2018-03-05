import pandas as pd
import folium

unemployment = pd.read_csv('data/US_Unemployment_Oct2012.csv')

m = folium.Map([43,-100], zoom_start=4)

m.choropleth(
    geo_data=open('data/us_states.json').read(),
    data=unemployment,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    )
