import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ranking_10k_cleaned.csv', sep=";")

times_ts = df[["YearGroup", "Time_Sec"]].groupby(
    ["YearGroup"], as_index=False).mean()

sns.lineplot(data=times_ts, x="YearGroup", y="Time_Sec")
sns.scatterplot(data=times_ts, x="YearGroup", y="Time_Sec")
plt.title("Avg. Running Times in History for 10000m")
plt.ylabel("Avg. Running Times (in seconds)")
plt.xlabel("Year of Event")
plt.show()

age_ts = df[["AgeGroup", "Time_Sec"]].groupby(
    ["AgeGroup"], as_index=False).mean()

sns.lineplot(data=age_ts, x="AgeGroup", y="Time_Sec")
sns.scatterplot(data=age_ts, x="AgeGroup", y="Time_Sec")
plt.title("Avg. Running Times in History for 10000m")
plt.ylabel("Avg. Running Times (in seconds)")
plt.xlabel("Age of the Athlete")
plt.show()
