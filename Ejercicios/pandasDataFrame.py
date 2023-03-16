import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("//home//juancho//Documents//Personalizadas//DataScience//GCB2022v27_MtCO2_flat.csv")

df.set_index("Country", inplace=True)

mexico = df.loc["Mexico"]
mexico.set_index("Year", inplace=True)
mexico = mexico.drop("ISO 3166-1 alpha-3", axis=1)

globalData = df.loc["Global"]
globalData.set_index("Year", inplace=True)
globalData = globalData.drop("ISO 3166-1 alpha-3", axis=1)