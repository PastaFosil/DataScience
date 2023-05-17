import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

r = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=1v4RAmO9uknwrbeKU3r1kdfTKsVbbWrg1k4ASSXT")

url = "https://api.nasa.gov/neo/rest/v1/neo/browse"
misParams = {"api_key": "1v4RAmO9uknwrbeKU3r1kdfTKsVbbWrg1k4ASSXT",
             "start_date": "2023-04-01",
             "end_date": "2023-04-30"}

r2 = requests.get(url, params=misParams)

dict_data = r2.json()

dict_data.keys()

data = dict_data["near_earth_objects"]

df = pd.json_normalize(data)

df["estimated_diameter.kilometers.estimated_diameter_min"].hist()

url = "https://api.nasa.gov/planetary/earth/imagery"
misParams = {
            'lon':'-101.706720',
            'lat':'21.154030',
            'date':'2019-02-01',
            "api_key": "1v4RAmO9uknwrbeKU3r1kdfTKsVbbWrg1k4ASSXT",}
r3 = requests.get(url, params=misParams)

ima = Image.open(BytesIO(r3.content))