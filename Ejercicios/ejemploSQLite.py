import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sqlite3
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

database = '//home//juancho//Documents//Personalizadas//DataScience//database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)
#tables

countries = pd.read_sql("""SELECT *
                        FROM Country;""", conn)
#countries

leagues = pd.read_sql("""SELECT *
                        FROM League
                        JOIN Country ON Country.id = League.country_id;""", conn)
#leagues

teams = pd.read_sql("""SELECT *
                        FROM Team
                        ORDER BY team_long_name
                        LIMIT 10;""", conn)
#teams

player = pd.read_sql("""SELECT player_name, height
                        FROM Player
                        ORDER BY height ASC;""", conn)

playerUnique = pd.read_sql("""SELECT DISTINCT height, player_name
                        FROM Player
                        ORDER BY height ASC;""", conn)