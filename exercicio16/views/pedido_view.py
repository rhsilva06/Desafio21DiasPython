
from models.cliente import Cliente
from models.produto import Produto
from models.pedido import Pedido
from utils.util import Util


class PedidoView():

    @staticmethod
    def busca_por_id_pedido():

        id_pedido = Util.campo_numerico("Id do Pedido")
        resultado = Pedido.obtem_por_id_pedido(id_pedido)

        if resultado == None:
            print(
                f"{Util.WARNING}Não foi encontrado nenhum pedido para o Id Pedido {id_pedido} no sistema.{Util.ENDC}")

        else:
            print(
                f"{Util.OKBLUE}============================[Resultado de Pedidos]============================{Util.ENDC}")

            print(f"{Util.OKBLUE}Id Produto: {resultado.id_produto}{Util.ENDC}")
            print(f"{Util.OKBLUE}Nome: {resultado.nome_produto}{Util.ENDC}")
            print(f"{Util.OKBLUE}Descrição: {resultado.descricao}{Util.ENDC}")
            print(f"{Util.OKBLUE}Preço: {resultado.preco}{Util.ENDC}")
            print(
                "------------------------------------------------------------------------------")

    @staticmethod
    def relatorio():

        lista = Pedido.obtem_todos()
        if len(lista) == 0:
            print(
                f"{Util.WARNING}Nenhum Pedido cadastrado no sistema.{Util.ENDC}")

        else:
            print(
                f"{Util.OKBLUE}============================[Relatório de Pedidos]============================{Util.ENDC}")

            for item in lista:
                print(f"{Util.CYELLOW2}Id Pedido: {item.id_pedido}{Util.ENDC}")
                print(f"{Util.CYELLOW2}Nome Cliente: {item.cliente.nome}{Util.ENDC}")
                print("{}Total: R$ {:0.4f} {}".format(
                    Util.CYELLOW2, item.total, Util.ENDC))
                print(
                    f"{Util.OKBLUE}------------------------------------------------------------------------------{Util.ENDC}")

                for p in item.itens:
                    print(
                        f"{Util.CYELLOW2}Id produto: {p.id_produto}{Util.ENDC}")
                    print(
                        f"{Util.CYELLOW2}Nome produto: {p.nome_produto}{Util.ENDC}")
                    print(
                        f"{Util.CYELLOW2}Descrição: {p.descricao}{Util.ENDC}")
                    print("{}Preço: {:0.4f} {}".format(
                        Util.CYELLOW2, p.preco, Util.ENDC))
                    print(
                        f"{Util.OKBLUE}------------------------------------------------------------------------------{Util.ENDC}")

    @staticmethod
    def __formulario_itens(cliente):
        itens = []
        try:
            while True:
                id_produto = Util.campo_numerico("Id do Produto")
                produto = Produto.obtem_produto_por_id(id_produto)
                if len(produto) == 0:
                    raise TypeError("Produto não encontrado.")

                itens.append(produto[0])
                print(
                    f"Deseja fazer incluir um novo produto para o cliente {cliente.nome} ?")
                print("1 - Sim")
                print("2 - Não")

                opcao_selecionada = Util.obtem_opcao_menu(1, 2)
                if opcao_selecionada == 0 or opcao_selecionada == 2:
                    return itens

        except TypeError as e:
            print(f"{Util.WARNING}Alerta: {e}{Util.ENDC}")
            PedidoView.__formulario_itens(cliente)
        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return None

    def __formulario(self, exibe_cabecalho=True):
        if(exibe_cabecalho == True):
            print(
                f"{Util.OKBLUE}============================[Cadastro de Pedidos]============================{Util.ENDC}")

            try:

                # obtem cliente
                email = Util.campo_email("E-mail")
                cliente_selecionado = Cliente.obtem_por_email(email)
                if len(cliente_selecionado) == 0:
                    print(
                        f"{Util.WARNING}Alerta: Cliente não encontrado.{Util.ENDC}")
                    return None

                # obtem lista de produtos
                print(
                    f"{Util.OKBLUE}============================[Lista de Produtos]============================{Util.ENDC}")
                produtos = Produto.obtem_todos()
                for produto in produtos:
                    print(
                        f"{Util.OKBLUE}Id Produto: {produto.id_produto}{Util.ENDC}")
                    print(
                        f"{Util.OKBLUE}Nome Produto: {produto.nome_produto}{Util.ENDC}")
                    print(f"{Util.OKBLUE}Descrição: {produto.descricao}{Util.ENDC}")
                    print("{}Preço: {:0.4f} {}".format(
                        Util.OKBLUE, produto.preco, Util.ENDC))
                    print(
                        f"{Util.OKBLUE}---------------------------------------------------------------------------{Util.ENDC}")

                itens = PedidoView.__formulario_itens(cliente_selecionado[0])
                if len(itens) == 0 or itens == None:
                    raise Exception(
                        f"Erro: Não foi possível gerar a lista de itens do pedido.")

                self.cliente = cliente_selecionado[0]
                self.itens = itens

                return self

            except TypeError as e:
                print(f"{Util.WARNING}Alerta: {e}{Util.ENDC}")
            except Exception as e:
                print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
                return None

    def cadastro(self):
        try:
            resultado = self.__formulario()

            if resultado == None:
                raise Exception(
                    "Não foi possível criar o objeto para cadastro.")

            pedido = Pedido()
            pedido.cliente = resultado.cliente
            pedido.itens = resultado.itens

            if pedido.salvar_arquivo() == True:
                print(f"{Util.OKGREEN}Pedido cadastrado com sucesso.{Util.ENDC}")

            while True:
                print("Deseja cadastar novo Pedido ?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")

                opcao_selecionada = Util.obtem_opcao_menu(1, 2)
                if opcao_selecionada == 1:
                    resultado = self.__formulario()
                    if resultado != None:

                        pedido.cliente = resultado.cliente
                        pedido.itens = resultado.itens

                        if pedido.salvar_arquivo() == True:
                            print(
                                f"{Util.OKGREEN}Produto cadastrado com sucesso.{Util.ENDC}")

                if opcao_selecionada == 0 or opcao_selecionada == 2:
                    Util.limpar_tela()
                    return True

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False
