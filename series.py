import pandas as pd

# Series
actas = pd.Series(["Acta de escrutinio y cómputo", "Acta de cómputo de votos adicionales", 
                   "Acta de la jornada electoral", "Acta de cómputo distrital", "Constancia de resultados"])
print("\nSerie de actas con índice automatico: ")
print(actas)

actas0 = pd.Series(["Acta de escrutinio y cómputo", "Acta de cómputo de votos adicionales", 
                   "Acta de la jornada electoral", "Acta de cómputo distrital", "Constancia de resultados"],
                   index=(1, 2, 3, 4, 5))
print("\nSeries de actas con índice personalizado, usamos index=(1, 2, 3, 4, 5):")
print(actas0)

print("\nObjetener elemento con indice 1, usamos index=(1, 2, 3, 4, 5), es:")
print(actas0[1])  


# dataframe con la series actas
print("\nDataFrame de actas y sus siglas:")
df = pd.DataFrame(actas)
print(df)