
from models.cliente import Cliente
from utils.util import Util


class ClienteView():

    @staticmethod
    def busca_por_email():

        email = Util.campo_email("E-mail")
        resultado = Cliente.obtem_por_email(email)

        if resultado == None:
            print(
                f"{Util.WARNING}Não foi encontrado nenhum cliente com o e-mail {email} no sistema.{Util.ENDC}")

        else:
            print(
                f"{Util.OKBLUE}============================[Resultado de Clientes]============================{Util.ENDC}")

            print(f"{Util.OKBLUE}Id: {resultado.id_cliente}{Util.ENDC}")
            print(f"{Util.OKBLUE}Nome: {resultado.nome}{Util.ENDC}")
            print(f"{Util.OKBLUE}E-mail: {resultado.email}{Util.ENDC}")
            print(
                "------------------------------------------------------------------------------")

    @staticmethod
    def verifica_email():
        try:
            while True:
                email = Util.campo_email("E-mail")
                resultado = Cliente.obtem_por_email(email)
                if len(resultado) > 0:
                    raise TypeError("E-mail já cadastrado.")

                return email
        except TypeError as e:
            print(f"{Util.WARNING}Alerta: {e}{Util.ENDC}")
            return ClienteView.verifica_email()

    @staticmethod
    def relatorio():

        lista = Cliente.obtem_todos()
        if len(lista) == 0:
            print(
                f"{Util.WARNING}Nenhum cliente cadastrado no sistema.{Util.ENDC}")

        else:
            print(
                f"{Util.OKBLUE}============================[Relatório de Clientes]============================{Util.ENDC}")

            for item in lista:
                print(f"{Util.CYELLOW2}Id: {item.id_cliente}{Util.ENDC}")
                print(f"{Util.CYELLOW2}Nome: {item.nome}{Util.ENDC}")
                print(f"{Util.CYELLOW2}E-mail: {item.email}{Util.ENDC}")
                print(
                    f"{Util.OKBLUE}------------------------------------------------------------------------------{Util.ENDC}")

    def __formulario(self, exibe_cabecalho=True):
        if(exibe_cabecalho == True):
            print(
                f"{Util.OKBLUE}============================[Cadastro de Clientes]============================{Util.ENDC}")

            try:

                self.nome = Util.campo_texto("Nome")
                self.email = ClienteView.verifica_email()
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

            cliente = Cliente()
            cliente.nome = resultado.nome
            cliente.email = resultado.email

            if cliente.salvar_arquivo() == True:
                print(f"{Util.OKGREEN}Cliente cadastrado com sucesso.{Util.ENDC}")

            while True:
                print("Deseja cadastar novo Cliente ?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")

                opcao_selecionada = Util.obtem_opcao_menu(1, 2)
                if opcao_selecionada == 1:
                    resultado = self.__formulario()
                    if resultado != None:
                        cliente.nome = resultado.nome
                        cliente.email = resultado.email
                        if cliente.salvar_arquivo() == True:
                            print(
                                f"{Util.OKGREEN}Cliente cadastrado com sucesso.{Util.ENDC}")

                if opcao_selecionada == 0 or opcao_selecionada == 2:
                    Util.limpar_tela()
                    return True

        except Exception as e:
            print(f"{Util.FAIL}Erro: {e}{Util.ENDC}")
            return False
