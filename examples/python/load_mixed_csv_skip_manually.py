import pandas as pd

filename = "examples/data/mixed.csv"
df = pd.read_csv(filename, skiprows=7, skipfooter=4, engine="python")
print(df)

