from utils.util import Util
from db.database import Database


class Produto():
    def __init__(self, id_produto="", nome_produto="", descricao="", preco=""):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.preco = preco

    @staticmethod
    def __to_object(itens):
        try:
            resultado = [Produto(val[0], val[1], val[2], val[3])
                         for val in itens]
            return resultado
        except:

            return []

    @staticmethod
    def obtem_todos():

        try:
            query_sql = "Select id_produto, nome_produto, descricao, preco from produtos order by nome_produto"
            resultado = Database.consultar(query_sql)
            return Produto.__to_object(resultado)

        except:
            return []

    @ staticmethod
    def obtem_produto_por_id(id_produto):
        query_sql = f"Select id_produto, nome_produto, descricao, preco from produtos where id_produto = {id_produto}"
        resultado = Database.consultar(query_sql)
        return Produto.__to_object(resultado)

    @ staticmethod
    def obtem_produto_por_nome(nome_produto):
        query_sql = f"Select id_produto, nome_produto, descricao, preco from produtos where id_produto like '{nome_produto}'"
        resultado = Database.consultar(query_sql)
        return Produto.__to_object(resultado)

    def salvar_arquivo(self):
        try:

            query_sql = f"INSERT INTO Produtos (nome_produto, descricao, preco) VALUES ('{self.nome_produto}','{self.descricao}',{self.preco})"
            Database.executar(query_sql)

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False
        finally:
            return True
