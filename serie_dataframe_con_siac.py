import pandas as pd

from conexionBD import conexionBD


class serie_dataframe_con_siac:

    def __init__(self):
        self.bd = conexionBD()

    def obtener_serie(self):
        consulta = """
            SELECT nombre_acta
            FROM siac.ttipo_acta
        """

        df = pd.read_sql(consulta, self.bd.conexion)

        serie = df["nombre_acta"]

        print("\nSerie de nombres de actas:")
        print(serie)

    def obtener_dataframe(self):
        consulta = """
            SELECT nombre_acta, siglas_acta
            FROM siac.ttipo_acta
        """

        dataframe = pd.read_sql(consulta, self.bd.conexion)

        print("\nDataFrame de actas y sus siglas:")
        print(dataframe)

    def cerrar(self):
        self.bd.cerrar()


# Ejecución

objeto = serie_dataframe_con_siac()

objeto.obtener_serie()

objeto.obtener_dataframe()

objeto.cerrar()