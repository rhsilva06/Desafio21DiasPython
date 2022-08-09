from utils.util import Util
from db.database import Database


class Cliente():
    def __init__(self, id_cliente="", nome="", email=""):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email

    @staticmethod
    def __to_object(itens):
        try:
            lista = [Cliente(val[0], val[1], val[2]) for val in itens]
            return lista
        except:
            return []

    @staticmethod
    def obtem_todos():

        try:

            query_sql = "Select id_cliente, nome, email from clientes order by nome"
            resultado = Database.consultar(query_sql)
            return Cliente.__to_object(resultado)

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False

    @ staticmethod
    def obtem_por_email(email):

        try:

            query_sql = f"Select id_cliente, nome, email from clientes where email = '{email}'"
            resultado = Database.consultar(query_sql)
            return Cliente.__to_object(resultado)

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False

    def salvar_arquivo(self):
        try:

            query_sql = f"INSERT INTO clientes (nome, email) VALUES ('{self.nome}', '{self.email}')"
            Database.executar(query_sql)

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False
        finally:
            return True
