import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dropCol(df):
    return df.drop("ISO 3166-1 alpha-3", axis=1)

def fillNan(df):
    return df.fillna(0)

df = pd.read_csv("//home//juancho//Documents//Personalizadas//DataScience//GCB2022v27_MtCO2_flat.csv")
df.set_index("Country", inplace=True)

print("\n===============================\n")
#NOMBRES
print("Nombres de columnas: ")
print(df.columns)

print("\n===============================\n")
#DATOS
print("Tipos de datos: ")
print(df.dtypes)

print("\n===============================\n")
#DISTRIBUCION DE NAN
print("Distribucion de NaNs: ")
"""
df = df.groupby(level=0).sum()

print("%i nan en columnas" % (df.isna().sum(axis=1)).groupby(level=0).sum())
print("%i nan en filas" % df.isna().sum(axis=0))
"""
df.info()

print("\n===============================\n")
#NUMERO DE PAISES
print("Datos de %i paises diferentes" % df.index.nunique())

print("\n===============================\n")
#MEXICO Y EL MUNDO
mexico = df.loc["Mexico"]
mexico.set_index("Year", inplace=True)
mexico = mexico.drop("ISO 3166-1 alpha-3", axis=1)
mexico = mexico.fillna(0)

globalData = df.loc["Global"]
globalData.set_index("Year", inplace=True)
globalData = globalData.drop("ISO 3166-1 alpha-3", axis=1)
globalData = globalData.fillna(0)

print("\n===============================\n")
#GRAFIQUITAS
f1 = plt.figure(1)
plt.title("Total")
plt.stackplot(mexico.index, mexico["Total"], globalData["Total"])
plt.legend(["Mexico", "Global"], loc="upper left")

f2 = plt.figure(2)
plt.title("Datos de Mexico")
plt.stackplot(mexico.index, [mexico[i] for i in mexico.columns[1:-1]])
plt.legend(mexico.columns[1:-1], loc="upper left")

f3 = plt.figure(3)
plt.title("Datos globales")
plt.stackplot(globalData.index, [globalData[i] for i in globalData.columns[1:-1]])
plt.legend(globalData.columns[1:-1], loc="upper left")

f4 = plt.figure(4)
plt.title("Datos per capita")
plt.plot(mexico.index, mexico[mexico.columns[-1]])
plt.plot(globalData.index, globalData[globalData.columns[-1]])
plt.legend(["Mexico", "Global"], loc="upper left")

plt.show()

print("\n===============================\n")
#G20
s = "Argentina, Australia, Brazil, Canada, China, France, Germany, India, Indonesia, Italy, South Korea, Japan, Mexico, Russia, Saudi Arabia, South Africa, Turkey, United Kingdom, USA"
g20Names = s.split(", ")

g20 = [df.loc[i] for i in g20Names]
for i in g20:
    i.set_index("Year", inplace=True)

g20 = list(map(dropCol, g20))
g20 = list(map(fillNan, g20))


color = ["#800000","#FF0000","#FF7F50","#CD5C5C","#FFA500","#FFD700","#BDB76B","#7CFC00","#90EE90","#8FBC8F","#66CDAA","#008080","#00FFFF","#6495ED","#0000FF","#8A2BE2","#FF69B4","#D2691E","#B0C4DE"]
cols = g20[0].columns
df = dropCol(df.loc[g20Names])
df = df.fillna(0)
df = df.groupby(level=0).sum()
g20max = []
f = list(range(len(cols)))
for i in range(len(cols)):
    g20max.append(list(df[cols[i]].sort_values(ascending=False).head(3).index))
        
    f[i] = plt.figure(i)
    plt.title(cols[i])
    plt.stackplot(g20[0].index, [g20[j][cols[i]] for j in range(len(g20))], colors=color)
    plt.legend(g20Names, loc="upper left")
plt.show()

g20max = np.array(g20max)
head = pd.DataFrame(index=cols, columns=np.arange(1,4,1), data=g20max)
print(head)

total = g20[0]
for i in g20[1:]:
    total = pd.merge(total,i, left_index=True,right_index=True).sort_index()
    total = total.rename(columns=dict(zip(total.columns, list(cols)*2)))
    total = total.transpose()
    total = total.groupby(level=0).sum()
    total = total.transpose()

ratio = total - mexico
mexico /= total
mexico = mexico.fillna(0)
ratio /= total
ratio = ratio.fillna(0)

cols = mexico.columns[:-1]
f = list(range(len(cols)))
for i in range(len(cols)):
    f[i] = plt.figure(i)
    plt.title(cols[i])
    plt.stackplot(mexico.index, mexico[cols[i]], ratio[cols[i]])
    plt.legend(["Mexico", "G20"], loc="upper left")
plt.show()