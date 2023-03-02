import numpy as np
import pandas as pd

letters = []
for i in range(97, 123):
    letters.append(chr(i))
print(letters)

x = np.arange(10, 10+len(letters))

A = pd.Series(data=x, index=letters)
print(A)

letters.reverse()
B = pd.Series(data=letters, index=x)
print(B)

print("A:")
print(A["d":"i"])

print("B:")
print(B[np.arange(27,33)])
print(B[B.isin(letters[17:23])])