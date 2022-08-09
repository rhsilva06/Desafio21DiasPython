''''
Faça um programa para calcular os valores de um pedido
para isso crie uma classe de pedido que tenha relação com uma classe de cliente
nesse pedido, coloque uma propriedade de itens, contendo instancias de uma classe de produto
no pedido, crie um método para calcular o valor total 
e um método para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá na classe de pedido:
- id
- cliente
- metodo_valor_total()
- itens []
O que terá na classe cliente:
- Nome
- email
O que terá na classe produto:
- Nome
- descrição
- preço
'''

from utils.util import Util
from controllers.cliente_controller import ClienteController
from controllers.produto_controller import ProdutoController
from controllers.pedido_controller import PedidoController
from controllers.relatorio_controller import RelatorioController


def main():
    cliente_controller = ClienteController()
    produto_controller = ProdutoController()
    pedido_controller = PedidoController()
    relatorio_controller = RelatorioController()

    while True:
        print(
            "============================[Sistema de Pedidos]============================")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Cadastrar Pedido")
        print("4 - Relatórios")
        print("5 - Sair do programa")
        print(
            "============================================================================")

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


main()
