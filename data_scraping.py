import pandas as pd 

df_list = []

url= 'https://www.worldathletics.org/records/all-time-toplists/middle-long/10000-metres/outdoor/men/senior?regionType=world&page={}&bestResultsOnly=true&firstDay=1899-12-31&lastDay=2021-04-27'

for i in range(60):
    dframe = pd.read_html(url.format(i),header=None)[0]
    df_list.append(dframe)


df = pd.concat(df_list)
df.to_csv('ranking_10000.csv')