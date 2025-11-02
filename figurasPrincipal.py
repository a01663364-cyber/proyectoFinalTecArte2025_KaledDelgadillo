import pandas as pd

# Leer el archivo separado por tabulaciones
dataFile = pd.read_csv("figuras.csv", sep="\t")

dataFile.columns = dataFile.columns.str.strip().str.upper()

# Limpiar nombres de columnas
dataFile ["MEDIDA1"] = pd.to_numeric(dataFile["MEDIDA1"], errors="coerce")
if "MEDIDA2" in dataFile.columns:
        dataFile ["MEDIDA2"] = pd.to_numeric(dataFile["MEDIDA2"], errors="coerce")

# Funciones para las áreas
def triangulo (base, altura):
        return (base * altura) / 2
def rectangulo (base, altura):
        return base * altura
def circulo(radio):
        return 3.1416 * (radio ** 2)

# Lista de resultados
areas = []

# Recorrer filas
for index, row in dataFile.iterrows ():
        figura = str(row["FIGURA"] ).strip().lower()

# Traducir letras a nombres completos
        if figura == "t":
                figura = "triangulo"
        elif figura == "r":
                figura = "rectangulo"
        elif figura == "c":
                figura = "circulo"

        medida1 = row["MEDIDA1"]
        medida2 = row.get ("MEDIDA2", None)

        area = None
        if figura == "triangulo" and pd.notna (medida1) and pd.notna (medida2):
                area = triangulo(medida1, medida2)
        elif figura == "rectangulo" and pd.notna(medida1) and pd.notna(medida2):
                area = rectangulo (medida1, medida2)
        elif figura == "circulo" and pd.notna(medida1):
                area = circulo (medida1)

        areas.append(area)

        if area is not None:
                print(f"Fila {index}: FIGURA={figura}, Área={area: .2f}")
        else:
                print(f"Fila {index}: Datos incompletos o figura no reconocida → FIGURA={row['FIGURA']}")

# Agregar columna con áreas
dataFile["AREA"] = areas
print("\n--- Tabla final con áreas ---")
print (dataFile)
