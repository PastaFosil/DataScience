import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium


df = pd.read_csv('//home//juancho//Documents//Personalizadas//DataScience//GCB2022v27_MtCO2_flat.csv')

df.head()

countries_geo = f'/home/juancho/Documents/Personalizadas/DataScience/countries.json'

df = df.drop(df[((df["Country"] == "Global") | (df["Country"] == "International Transport"))].index)

data_map = df.groupby('ISO 3166-1 alpha-3')['Total'].max()

data_map = pd.DataFrame(data_map).reset_index()
data_map.head()

data_map.Total.max()

m = folium.Map(location=[22, -50], zoom_start=2, width='100%', height='100%',position='bottomLeft')

folium.Choropleth(
    geo_data=countries_geo,
    name='choropleth',
    data=data_map,
    columns=['ISO 3166-1 alpha-3', 'Total'],
    key_on='feature.properties.ISO_A3',
    fill_color='YlGnBu', #'BuPu',
    fill_opacity=0.9,
    line_opacity=0.2,
    nan_fill_color = 'white',
    line_color="purple", 
    line_weight=1,
    legend_name='Emisiones Totales',
).add_to(m)

folium.LayerControl().add_to(m)

m.save("emissions1.html")