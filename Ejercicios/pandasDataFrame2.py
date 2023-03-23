import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def changeDType(df):
    cols = df.columns
    if "Z" in cols:
        cols = [l for l in list(cols) if l!="Z"]
    
    for i in cols:
        df[i] = df[i].astype("int64")

    return df

nums = np.random.randint(100, 3000, (8, 4))
letters = np.reshape(list("abcd")*2, (8,1))
values = np.append(nums, letters, axis = 1)

fecha = pd.date_range("20230915", periods=8)

df = pd.DataFrame(values, index=fecha, columns=list("VWXYZ"))