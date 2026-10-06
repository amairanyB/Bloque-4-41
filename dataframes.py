import pandas as pd

# dataframe de actas y sus siglas
df = pd.DataFrame({
    "siglas_acta": ["AEC", "ACVA", "AJE", "ACD", "CR"],
    "nombre_acta": [
        "Acta de escrutinio y cómputo",
        "Acta de cómputo de votos adicionales",
        "Acta de la jornada electoral",
        "Acta de cómputo distrital",
        "Constancia de resultados"
    ]
})
print("\nDataFrame de actas y sus siglas:")
print(df)

# Dataframe con índice personalizado
# DataFrame de actas y sus siglas
df = pd.DataFrame({
    "siglas_acta": ["AEC", "ACVA", "AJE", "ACD", "CR"],
    "nombre_acta": [
        "Acta de escrutinio y cómputo",
        "Acta de cómputo de votos adicionales",
        "Acta de la jornada electoral",
        "Acta de cómputo distrital",
        "Constancia de resultados"
    ]
}, index=range(1, 6))

print("\nDataFrame de actas y sus siglas con indice personalizado:")
print(df)

#  .loc para obtener un elemento del DataFrame
print("\nObtener elemento con .loc, usamos index=range(1, 6), es:")
print(df.loc[3])
