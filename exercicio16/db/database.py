import pyodbc
import os


class Database():

    @staticmethod
    def __get_connection_string():
        return f"Driver=SQL Server;Server={os.getenv('HOST_DESAFIO_PYTHON')};Database={os.getenv('BASE_DESAFIO_PYTHON')};Trusted_Connection=yes;"

    @staticmethod
    def consultar(query_sql):

        try:
            server = Database.__get_connection_string()
            conexao = pyodbc.connect(server)
            cursor = conexao.cursor()
            cursor.execute(query_sql)
            resultado = cursor.fetchall()
            return resultado

        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conexao.close()

    @staticmethod
    def executar(query_sql):
        try:

            server = Database.__get_connection_string()
            conexao = pyodbc.connect(server)
            cursor = conexao.cursor()
            cursor.execute(query_sql)
            cursor.execute("SELECT @@IDENTITY AS ID;")
            id = int(cursor.fetchone()[0])
            conexao.commit()
            return id

        except Exception as e:
            print(f"Erro: {e}")
            return None
        finally:
            conexao.close()
