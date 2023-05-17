import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
#Análisis de los datos de la variación porcentual de la actividad económica total de cada entidad
#del tercer trimestre del año (2022) respecto al trimestre anterior
df = pd.DataFrame(pd.read_csv('//home//juancho//Documents//Personalizadas//DataScience//variacionActividadMex.csv'))
#df = df.set_index("Entidad federativa",inplace=True)
df1 = pd.DataFrame({"Entidad federativa":df["Entidad federativa"],"Promedio":df[df.columns[1:]].mean(axis=1)})

statesURL = ("https://www.gits.igg.unam.mx/repositoriodecapas/geojson/u_territorial_estados_mgn_inegi_2013.json")

m = folium.Map(location=[24, -102], zoom_start=6, width='100%', height='100%',position='bottomLeft')
#folium.GeoJson(statesURL).add_to(m)

folium.Choropleth(
    geo_data=statesURL,
    name='choropleth',
    data=df1,
    columns=["Entidad federativa", "Promedio"],
    key_on='feature.properties.nom_ent',
    fill_color='YlGnBu', #'BuPu',
    fill_opacity=0.9,
    line_opacity=0.2,
    nan_fill_color = 'white',
    line_color="purple", 
    line_weight=1,
    legend_name='Variación porcentual promedio',
).add_to(m)

m.save("mex.html")

regions = {"Región Norte": ['Baja California', 'Baja California Sur', 'Coahuila de Zaragoza', 'Chihuahua', 'Nuevo León', 'Sinaloa', 'Sonora', 'Tamaulipas'],
           "Región Centro-Norte": ['Aguascalientes', 'Colima', 'Durango', 'Guanajuato', 'Jalisco', 'Nayarit', 'San Luis Potosí', 'Zacatecas'],
           "Región Centro": ["Distrito Federal", "México"],
           "Región Centro-Sur": ['Guerrero', 'Hidalgo', 'Michoacán de Ocampo', 'Morelos', 'Puebla', 'Querétaro', 'Tlaxcala'],
           "Región Sur-Sureste": ['Campeche', 'Chiapas', 'Oaxaca', 'Quintana Roo', 'Tabasco', 'Veracruz de Ignacio de la Llave', 'Yucatán']
        }

df["Región"] = ["Nacional","Región Centro-Norte","Región Norte","Región Norte","Región Sur-Sureste","Región Norte","Región Centro-Norte","Región Sur-Sureste","Región Norte","Región Centro","Región Centro-Norte","Región Centro-Norte","Región Centro-Sur","Región Centro-Sur","Región Centro-Norte","Región Centro","Región Centro-Sur","Región Centro-Sur","Región Centro-Norte","Región Norte","Región Sur-Sureste","Región Centro-Sur","Región Centro-Sur","Región Sur-Sureste","Región Centro-Norte","Región Norte","Región Norte","Región Sur-Sureste","Región Norte","Región Centro-Sur","Región Sur-Sureste","Región Sur-Sureste","Región Centro-Norte"]
#df = df.rename(columns={"1T":1,"2T":2,"3T":3})

df1 = pd.melt(df,id_vars=["Región"], value_vars=df.columns[1:])
df1 = df1.rename(columns={"variable":"Trimestre","value":"Variacion porcentual"})

sns.violinplot(data=df1, x="Variacion porcentual", y="Trimestre",palette="plasma")
sns.swarmplot(data=df1, x="Variacion porcentual", y="Trimestre",size=6,hue="Región", palette="plasma" )
plt.show()