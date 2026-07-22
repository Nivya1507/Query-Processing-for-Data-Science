import pandas as pd

df = pd.read_csv("jobs.csv")
sorted_df = df.sort_values(by="JOB_TITLE", ascending=False)

print(sorted_df)
