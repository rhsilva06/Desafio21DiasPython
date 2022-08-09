from controllers.cliente_controller import ClienteController
from controllers.produto_controller import ProdutoController
from controllers.pedido_controller import PedidoController
from utils.util import Util


class RelatorioView():

    @staticmethod
    def relatorio():
        while True:
            print(
                f"{Util.OKBLUE}=================================[Relatórios]================================={Util.ENDC}")
            print(f"{Util.OKBLUE}1 - Relatórios de Clientes{Util.ENDC}")
            print(f"{Util.OKBLUE}2 - Relatórios de Produtos{Util.ENDC}")
            print(f"{Util.OKBLUE}3 - Relatórios de Pedidos{Util.ENDC}")
            print(f"{Util.OKBLUE}0 - Voltar ao menu principal{Util.ENDC}")
            print(
                f"{Util.OKBLUE}=============================================================================={Util.ENDC}")

            menu = Util.obtem_opcao_menu(1, 3)

            if menu == 1:
                # Relatório de Cliente
                Util.limpar_tela()
                cliente_controller = ClienteController()
                cliente_controller.relatorio()
            elif menu == 2:
                # Relatório de Produtos
                Util.limpar_tela()
                produto_controller = ProdutoController()
                produto_controller.relatorio()
            elif menu == 3:
                # Relatório de Pedido
                Util.limpar_tela()
                pedido_controller = PedidoController()
                pedido_controller.relatorio()
            elif menu == 0:
                # Menu principal
                Util.limpar_tela()
                return
