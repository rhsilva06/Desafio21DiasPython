from utils.util import Util
from db.database import Database
from datetime import date
from models.cliente import Cliente
from models.produto import Produto


class Pedido():
    def __init__(self):
        self.id_pedido = 0
        self.cliente = None
        self.itens = []
        self.total = 0

    def __to_object(itens):

        lista_produto = []
        lista_pedido = []
        lista_pedido_item_somado = []
        soma_total_pedido = 0

        for index, elem in enumerate(itens):
            curr_item = itens[index]
            next_item = itens[(index + 1) % len(itens)]

            id_pedido_atual = curr_item[3]
            id_pedido_proximo = next_item[3]

            if id_pedido_atual == id_pedido_proximo:

                id_item = curr_item[5]
                resultado = any(
                    elem == id_item for elem in lista_pedido_item_somado)
                if resultado == False:
                    produto = Produto(
                        curr_item[7], curr_item[8], curr_item[9], curr_item[10])
                    lista_produto.append(produto)
                    lista_pedido_item_somado.append(id_item)
                    soma_total_pedido += float(curr_item[10])

                id_item = next_item[5]
                resultado = any(
                    elem == id_item for elem in lista_pedido_item_somado)
                if resultado == False:
                    produto = Produto(
                        next_item[7], next_item[8], next_item[9], next_item[10])
                    lista_produto.append(produto)
                    lista_pedido_item_somado.append(id_item)
                    soma_total_pedido += float(next_item[10])

            else:
                cliente = Cliente(curr_item[0], curr_item[1], curr_item[2])

                pedido = Pedido()
                pedido.id_pedido = curr_item[3]
                pedido.cliente = cliente
                pedido.itens = lista_produto

                pedido.total = soma_total_pedido
                lista_pedido.append(pedido)

                lista_produto = []
                lista_pedido_item_somado = []
                soma_total_pedido = 0

        return lista_pedido

    @ staticmethod
    def obtem_todos():

        try:
            query_sql = " select cli.id_cliente, "
            query_sql += " cli.nome, "
            query_sql += " cli.email, "
            query_sql += " ped.id_pedido, "
            query_sql += " ped.data_pedido, "
            query_sql += " pit.id_item, "
            query_sql += " pit.data_pedido_item, "
            query_sql += " pro.id_produto, "
            query_sql += " pro.nome_produto, "
            query_sql += " pro.descricao, "
            query_sql += " pro.preco "
            query_sql += " from clientes as cli "
            query_sql += " inner join pedidos as ped on (cli.id_cliente = ped.id_cliente) "
            query_sql += " inner join pedido_itens as pit on (ped.id_pedido = pit.id_pedido) "
            query_sql += " inner join produtos as pro on(pit.id_produto = pro.id_produto) "
            query_sql += " order by ped.data_pedido"

            resultado = Database.consultar(query_sql)
            return Pedido.__to_object(resultado)

        except:
            return []

    @ staticmethod
    def obtem_por_id_pedido(id_pedido):
        query_sql = " select cli.id_cliente, "
        query_sql += " cli.nome, "
        query_sql += " cli.email, "
        query_sql += " ped.id_pedido, "
        query_sql += " ped.data_pedido, "
        query_sql += " pit.id_item, "
        query_sql += " pit.data_pedido_item, "
        query_sql += " pro.id_produto, "
        query_sql += " pro.nome_produto, "
        query_sql += " pro.descricao, "
        query_sql += " pro.preco "
        query_sql += " from clientes as cli "
        query_sql += " inner join pedidos as ped on (cli.id_cliente = ped.id_cliente) "
        query_sql += " inner join pedido_itens as pit on (ped.id_pedido = pit.id_pedido) "
        query_sql += " inner join produtos as pro on(pit.id_produto = pro.id_produto) "
        query_sql += f" where ped.id_pedido = {id_pedido} "
        query_sql += " order by ped.data_pedido "
        resultado = Database.consultar(query_sql)
        return Pedido.__to_object(resultado)

    def salvar_arquivo(self):
        try:
            data_pedido = date.today()
            query_insert_pedido = f"insert into pedidos (id_cliente, data_pedido) values ({self.cliente.id_cliente}, {data_pedido})"
            resultado_id_pedido = Database.executar(query_insert_pedido)

            for item in self.itens:
                data_pedido_item = date.today()
                query_insert_itens_pedido = f"insert into pedido_itens(id_pedido, id_produto, data_pedido_item) values ({str(resultado_id_pedido)}, {str(item.id_produto)}, {data_pedido_item})"
                Database.executar(query_insert_itens_pedido)

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False
        finally:
            return True
