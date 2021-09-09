# Willian Reichert - 09/09/2021
import pandas as pd

data = pd.read_csv('gerint.csv', sep=';')

print(f"{data.info()}\n")
print(data[pd.isnull(data['idade'])])
