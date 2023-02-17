import numpy as np

B = np.array([[0.4, 0.41, 0.42, 0.43, 0.44],
     [0.45, 0.46, 0.47, 0.48, 0.49],
     [0.5, 0.51, 0.52, 0.53, 0.54],
     [0.55, 0.56, 0.57, 0.58, 0.59],
     [0.6, 0.61, 0.62, 0.63, 0.64],
     [0.65, 0.66, 0.67, 0.68, 0.69],
     [0.7, 0.71, 0.72, 0.73, 0.74],
     [0.75, 0.76, 0.77, 0.78, 0.79]])

columnas = np.empty((8,8), dtype="uint64")
for c in range(8):
    for f in range(1, 9):
        columnas[f-1,c] = c*8 + f

columnas = columnas.astype("str")

x = np.arange(0, 8)
for r in x:
    for c in x:
        y = "3" in columnas[r,c] 
        if y==True:
            columnas[r,c] = "-99"
columnas = columnas.astype("float64")

B = np.append(B, columnas, axis=1)
