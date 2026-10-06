# conexion BD
import psycopg

class conexionBD:
    def __init__(self):
        self.conexion = psycopg.connect(
            host = "localhost",
            port = 5432,
            dbname = "siac",
            user = "postgres",
            password = "123"
        )
        print("conexión exitosa a postgresql")

    def cerrar(self):
        self.conexion.close()
        print("conexion cerrada")