
from models.produto import Produto
from utils.util import Util


class ProdutoView():

    @staticmethod
    def busca_por_nome_produto():

        nome_produto = Util.campo_texto("Nome Produto")
        resultado = Produto.obtem_produto_por_nome(nome_produto)

        if resultado == None:
            print(
                f"{Util.WARNING}Não foi encontrado nenhum produto com nome {nome_produto} no sistema.{Util.ENDC}")

        else:
            print(
                f"{Util.OKBLUE}============================[Resultado de Produtos]============================{Util.ENDC}")

            print(f"{Util.OKBLUE}Id Produto: {resultado.id_produto}{Util.ENDC}")
            print(f"{Util.OKBLUE}Nome: {resultado.nome_produto}{Util.ENDC}")
            print(f"{Util.OKBLUE}Descrição: {resultado.descricao}{Util.ENDC}")
            print(f"{Util.OKBLUE}Preço: {resultado.preco}{Util.ENDC}")
            print(
                "------------------------------------------------------------------------------")

    @staticmethod
    def relatorio():

        lista = Produto.obtem_todos()
        if len(lista) == 0:
            print(
                f"{Util.WARNING}Nenhum Produto cadastrado no sistema.{Util.ENDC}")

        else:
            print(
                f"{Util.OKBLUE}============================[Relatório de Produtos]============================{Util.ENDC}")

            for item in lista:
                print(f"{Util.CYELLOW2}Id Produto: {item.id_produto}{Util.ENDC}")
                print(f"{Util.CYELLOW2}Nome Prodto: {item.nome_produto}{Util.ENDC}")
                print(f"{Util.CYELLOW2}Descrição: {item.descricao}{Util.ENDC}")
                print("{}Preço: {:0.4f} {}".format(
                    Util.CYELLOW2, item.preco, Util.ENDC))
                print(
                    f"{Util.OKBLUE}------------------------------------------------------------------------------{Util.ENDC}")

    def __formulario(self, exibe_cabecalho=True):
        if(exibe_cabecalho == True):
            print(
                f"{Util.OKBLUE}============================[Cadastro de Produtos]============================{Util.ENDC}")

            try:

                self.nome_produto = Util.campo_texto("Nome Produto")
                self.descricao = Util.campo_texto("Descrição")
                self.preco = Util.campo_float("Preço")

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

            produto = Produto()
            produto.nome_produto = resultado.nome_produto
            produto.descricao = resultado.descricao
            produto.preco = resultado.preco

            if produto.salvar_arquivo() == True:
                print(f"{Util.OKGREEN}Produto cadastrado com sucesso.{Util.ENDC}")

            while True:
                print("Deseja cadastar novo Produto ?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")

                opcao_selecionada = Util.obtem_opcao_menu(1, 2)
                if opcao_selecionada == 1:
                    resultado = self.__formulario()
                    if resultado != None:
                        produto.nome_produto = resultado.nome_produto
                        produto.descricao = resultado.descricao
                        produto.preco = resultado.preco

                        if produto.salvar_arquivo() == True:
                            print(
                                f"{Util.OKGREEN}Produto cadastrado com sucesso.{Util.ENDC}")

                if opcao_selecionada == 0 or opcao_selecionada == 2:
                    Util.limpar_tela()
                    return True

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False
