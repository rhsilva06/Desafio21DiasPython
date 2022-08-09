
from models.cliente import Cliente
from views.cliente_view import ClienteView


class ClienteController():
    def __init__(self):
        self.model = Cliente()
        self.view = ClienteView()

    def cadastro(self):
        self.view.cadastro()

    def relatorio(self):
        self.view.relatorio()

    def busca_por_email(self):
        self.view.busca_por_email()

    def start(self):
        self.view.cadastro()


if __name__ == "__main__":
    main = ClienteController()
    main.start()
