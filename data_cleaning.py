import pandas as pd
import datetime
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ranking_10k.csv', sep=";")

# drop 'Unnamed: 6' and 'Unnamed: 6' columns
df.drop(['Unnamed: 6', 'Column1'], axis='columns', inplace=True)

df.head()

# get a column with the year of the event
df["Date"] = df["Date"].astype(str)
df["DOB"] = df["DOB"].astype(str)

# df_split = df["Date"].apply(lambda x: x.split('/')[2])
# df["Year"] = df_split

df["Age"] = ((pd.to_datetime(df["Date"]) - pd.to_datetime(df["DOB"])
              ) / np.timedelta64(1, 'Y')).round()
df['Year_Event'] = pd.DatetimeIndex(pd.to_datetime(df["Date"])).year


# organize the dates of the events by year groups
def group_years(year):
    if year in range(1960, 1970):
        return "1960-1969"
    elif year in range(1970, 1980):
        return "1970-1979"
    elif year in range(1980, 1990):
        return "1980-1989"
    elif year in range(1990, 2000):
        return "1990-1999"
    elif year in range(2000, 2010):
        return "2000-2009"
    elif year in range(2010, 2020):
        return "2010-2019"
    else:
        return "2020+"


df["YearGroup"] = df["Year_Event"].apply(group_years)

# Organize the ages of the athletes by groups


def group_ages(age):
    if age in range(0, 20):
        return "0-19"
    elif age in range(20, 26):
        return "20-25"
    elif age in range(26, 31):
        return "26-30"
    elif age in range(31, 36):
        return "31-35"
    elif age in range(36, 41):
        return "36-41"
    else:
        return "40+"


df["AgeGroup"] = df["Age"].apply(group_ages)

# Convertion of running time to seconds
df["Mark"]
df_split1 = df["Mark"].apply(lambda x: x.split('.')[0])
df_split2 = (df["Mark"].astype(str)).apply(lambda x: x.split('.')[1])
df["Time"] = (df_split1) + ":" + (df_split2)

# x = pd.Series("Time")
# x.convert_dtypes()


def time_to_sec(time):
    try:
        return (datetime.datetime.strptime(time, "%M:%S:%f") - datetime.datetime(1900, 1, 1)).total_seconds()
    except:
        return (datetime.datetime.strptime(time, "%M:%S") - datetime.datetime(1900, 1, 1)).total_seconds()


df["Time_Sec"] = df["Time"].apply(time_to_sec)
