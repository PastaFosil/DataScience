import requests
import pandas as pd
import numpy as np
import re

pd.options.mode.chained_assignment = None
buscar_en_titulo = 'astro'
 
endpoint = 'https://es.wikipedia.org/w/rest.php/v1/search/title'

params = {
            'q' : buscar_en_titulo,
            'limit': 10
         }

astro = requests.get(endpoint, params=params)

astro.status_code

df = pd.json_normalize(astro.json()['pages'])

endpoint = 'https://es.wikipedia.org/w/api.php'

es100tifico = np.empty(0)
resumen = np.empty(0)
for i in df["title"]:
    params = {
            'action' : 'query',
            'format' : 'json',
            'titles' : i, 
            'prop' : 'extracts',
            'exintro': True,
            'explaintext': True
        }
    astro = requests.get(endpoint, params=params)

    df1 = pd.json_normalize(astro.json()['query'])
    resumen = np.append(resumen, df1[df1.keys()[-1]][0])

    regex = re.compile(r'(F(i|í)sica)|( Ciencia)', re.IGNORECASE)

    check = regex.search(resumen[-1])
    
    if check == None:   
        es100tifico = np.append(es100tifico, 0)
    else:
        es100tifico = np.append(es100tifico, 1)
    
    
    
    """
    for i in palabras:
        check = 1
        regex = re.compile(i, re.IGNORECASE)
        if regex.search(resumen) == None:
            check = np.max(check, 0)
    es100tifico = np.append(es100tifico, check)
    """
print(es100tifico)

final = df[["id", "title"]]
final["Resumen"] = np.reshape(resumen,[len(resumen),1])
final["Contiene palabra"] = np.reshape(es100tifico.astype("int64"),[len(es100tifico),1])
print(final)

