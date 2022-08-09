from controllers.cliente_controller import ClienteController
from controllers.produto_controller import ProdutoController
from controllers.pedido_controller import PedidoController
from controllers.relatorio_controller import RelatorioController
from utils.util import Util


class ProgramView():

    @staticmethod
    def init():
        cliente_controller = ClienteController()
        produto_controller = ProdutoController()
        pedido_controller = PedidoController()
        relatorio_controller = RelatorioController()

        while True:
            print(
                f"{Util.OKBLUE}=================================[Sistema de Pedidos]================================={Util.ENDC}")
            print(f"{Util.OKBLUE}1 - Cadastrar Cliente{Util.ENDC}")
            print(f"{Util.OKBLUE}2 - Cadastrar Produto{Util.ENDC}")
            print(f"{Util.OKBLUE}3 - Cadastrar Pedido{Util.ENDC}")
            print(f"{Util.OKBLUE}4 - Relatórios{Util.ENDC}")
            print(f"{Util.OKBLUE}5 - Sair do programa{Util.ENDC}")
            print(
                f"{Util.OKBLUE}======================================================================================{Util.ENDC}")

            menu = Util.obtem_opcao_menu(1, 5)

            if menu == 1:
                # Cadastro de Cliente
                Util.limpar_tela()
                cliente_controller.cadastro()
            elif menu == 2:
                # Cadastro de Produtos
                Util.limpar_tela()
                produto_controller.cadastro()
            elif menu == 3:
                # Cadastro de Pedido
                Util.limpar_tela()
                pedido_controller.cadastro()
            elif menu == 4:
                # relatórios
                Util.limpar_tela()
                relatorio_controller.relatorio()
            elif menu == 5:
                print("Sair do programa")
                break
