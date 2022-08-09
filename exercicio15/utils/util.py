import os
import re


class Util():

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'

    @staticmethod
    def limpar_tela():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def valida_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return True
        return False

    @staticmethod
    def campo_email(label):
        while True:
            valor_input = input(f"Digite o valor para o campo {label}: ")
            if valor_input.strip() == "":
                print(f"Alerta: Valor inválido. {label}")
                return Util.campo_email(label)

            if Util.valida_email(valor_input) == False:
                print(f"Alerta: E-mail inválido")
                return Util.campo_email(label)

            return valor_input

    @staticmethod
    def campo_texto(label):
        while True:
            valor_input = input(f"Digite o valor para o campo {label}: ")
            if valor_input.strip() == "":
                print(f"{Util.WARNING}Alerta: Valor inválido. {label}{Util.ENDC}")
                return Util.campo_texto(label)

            return valor_input

    @staticmethod
    def campo_numerico(label):
        while True:
            valor_input = input(f"Digite o valor para o campo {label}: ")
            if valor_input.isnumeric() == False:
                print(f"{Util.WARNING}Alerta: Valor inválido. {label}{Util.ENDC}")
                return Util.campo_numerico(label)

            return int(valor_input)

    @staticmethod
    def is_float(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False

    @staticmethod
    def campo_float(label):
        while True:
            valor_input = input(f"Digite o valor para o campo {label}: ")
            if Util.is_float(valor_input) == False:
                print(f"{Util.WARNING}Alerta: Valor inválido. {label}{Util.ENDC}")
                return Util.campo_float(label)

            return float(valor_input)

    @staticmethod
    def obtem_opcao_menu(incial, final):
        try:
            valor_convertido = Util.campo_numerico("Menu")
            if valor_convertido == 0:
                return 0
            elif valor_convertido >= incial and valor_convertido <= final:
                return valor_convertido
            else:
                raise TypeError("Opção inválida.")
        except TypeError as e:
            print(f"{Util.WARNING}Alerta: {e}{Util.ENDC}")
            return Util.obtem_opcao_menu(incial, final)
