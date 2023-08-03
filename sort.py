import pandas as pd

df = pd.read_csv('data.csv')
df = df.sort_values(by='Status')
df.to_csv('data.csv', index=False)
