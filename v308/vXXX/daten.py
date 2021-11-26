import pandas as pd

daten = pd.read_csv("daten_lange_spule.csv", sep=';')
print(daten.to_latex(index = False))