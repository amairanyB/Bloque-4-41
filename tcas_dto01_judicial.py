import pandas as pd

from conexionBD import conexionBD


class tcas_dto01_judicial:

    def __init__(self):
        self.bd = conexionBD()

    # Obtener el dataframe de la tabla tcas_dto01_judicial
    def obtener_dataframe(self):

        consulta = """
        SELECT * FROM siac.tcas_dto01_judicial
        """

        # hacer dataframe
        df = pd.read_sql(consulta, self.bd.conexion)

        print("\nDataFrame de tcas_dto01_judicial:")
        print(df)

        return df


objeto = tcas_dto01_judicial()

objeto.obtener_dataframe()

# obtener df.info y df.describe
objeto = tcas_dto01_judicial()

df = objeto.obtener_dataframe()

print("\n--- INFO ---")
df.info()

print("\n--- DESCRIBE ---")
print(df.describe())


#Obtener los valores vacios null por columna
print("\n--- VALORES VACIOS POR COLUMNA ---")
pd.set_option('display.max_rows', None)
print(df.isnull().sum())