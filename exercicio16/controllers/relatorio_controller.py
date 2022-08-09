from views.relatorio_view import RelatorioView


class RelatorioController():
    def __init__(self):
        self.view = RelatorioView()

    def relatorio(self):
        self.view.relatorio()

    def start(self):
        self.view.relatorio()


if __name__ == "__main__":
    main = RelatorioController()
    main.start()
