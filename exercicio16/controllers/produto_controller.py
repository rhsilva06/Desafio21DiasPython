
from models.produto import Produto
from views.produto_view import ProdutoView


class ProdutoController():
    def __init__(self):
        self.model = Produto()
        self.view = ProdutoView()

    def cadastro(self):
        self.view.cadastro()

    def relatorio(self):
        self.view.relatorio()

    def busca_por_nome_produto(self):
        self.view.busca_por_nome_produto()

    def start(self):
        self.view.cadastro()


if __name__ == "__main__":
    main = ProdutoController()
    main.start()
