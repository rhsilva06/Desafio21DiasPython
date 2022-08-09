
from models.pedido import Pedido
from views.pedido_view import PedidoView


class PedidoController():
    def __init__(self):
        self.model = Pedido()
        self.view = PedidoView()

    def cadastro(self):
        self.view.cadastro()

    def relatorio(self):
        self.view.relatorio()

    def busca_por_id_pedido(self):
        self.view.busca_por_id_pedido()

    def start(self):
        self.view.cadastro()


if __name__ == "__main__":
    main = PedidoController()
    main.start()
