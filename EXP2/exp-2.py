import pandas as pd
df = pd.read_csv("job_history.csv")
job_counts = df['EMPLOYEE_ID'].value_counts()
multiple_jobs = job_counts[job_counts >= 2].index
print(df[df['EMPLOYEE_ID'].isin(multiple_jobs)])
