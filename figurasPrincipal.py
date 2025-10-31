import pandas as pd

dataFile= ps.read_csv("figura.csv")


areas = []
perimetros = []

for index, roe in dataFile.iterrows():
	print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
