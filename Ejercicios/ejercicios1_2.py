import numpy as np

filas = np.empty((8,8), dtype="uint64")
for f in range(8):
    for c in range(1, 9):
        filas[f,c-1] = f*8 + c

print(filas)

print("")

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

print(columnas.astype("float64"))