import pandas as pd
df = pd.read_csv("employees.csv")
distinct_departments = df['DEPARTMENT_ID'].unique()

print(distinct_departments)
