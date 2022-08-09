from views.program_view import ProgramView


class ProgramController():
    def __init__(self):
        self.view = ProgramView()

    def init(self):
        self.view.init()

    def start(self):
        self.view.init()


if __name__ == "__main__":
    main = ProgramController()
    main.start()
