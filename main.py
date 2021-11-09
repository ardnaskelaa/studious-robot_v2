import pandas as pd

medals = r'medals.csv'

medals_r = pd.read_csv(medals, header=0)
r = pd.isnull(medals_r).sum()

print(r)