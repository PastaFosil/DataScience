import requests
import pandas as pd

url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Xoloitzcuintle&prop=extracts'

requestWiki = requests.get(url)
requestWiki.status_code

requestWiki.json().keys()

requestWiki.json()["query"].keys()

requestWiki.json()["query"]["pages"].keys()

requestWiki.json()["query"]["pages"]["243549"].keys()

df = pd.json_normalize(requestWiki.json()["query"])

df = pd.json_normalize(requestWiki.json()["query"]["pages"])

df = pd.json_normalize(requestWiki.json()["query"]["pages"]["243549"])


buscarTitulo = "Xoloitzcuintle"

endpoint = 'https://en.wikipedia.org/w/api.php'

params = {
            'action' : 'query',
            'format' : 'json',
            'titles' : buscarTitulo, 
            'prop' : 'extracts'
        }

request2_wiki = requests.get(endpoint, params=params)

request2_wiki.status_code

df = pd.json_normalize(request2_wiki.json()['query'])

params = {
            'action' : 'query',
            'format' : 'json',
            'titles' : buscarTitulo, 
            'prop' : 'extracts',
            'exintro': True,
            'explaintext': True
        }

request3_wiki = requests.get(endpoint, params=params)

request3_wiki.status_code

df = pd.json_normalize(request3_wiki.json()['query'])
resumen_xolo = df['pages.243549.extract'][0]




buscar_en_titulo = "Leon"

endpoint = 'https://es.wikipedia.org/w/api.php'

params = {
            'action' : 'query',
            'format' : 'json',
            'list':'search',
            'srsearch' : buscar_en_titulo
        }

request4_wiki = requests.get(endpoint, params=params)

request4_wiki.status_code

df = pd.json_normalize(request4_wiki.json()['query']['search'])



buscar_en_titulo = 'Leon'
 
endpoint = 'https://es.wikipedia.org/w/rest.php/v1/search/title'

params = {
            'q' : buscar_en_titulo,
            'limit': 10
         }

request5_wiki = requests.get(endpoint, params=params)

request5_wiki.status_code

df = pd.json_normalize(request5_wiki.json()['pages'])

endpoint = 'https://en.wikipedia.org/w/api.php'

for i in df["title"]:
    params = {
            'action' : 'query',
            'format' : 'json',
            'titles' : i, 
            'prop' : 'extracts',
            'exintro': True,
            'explaintext': True
        }

    requestLeon = requests.get(endpoint, params=params)

    df1 = pd.json_normalize(requestLeon.json()['query'])
    resumen = df1[df1.keys()[-1]][0]

    print("==========================================")
    print(i)
    print(resumen)    
