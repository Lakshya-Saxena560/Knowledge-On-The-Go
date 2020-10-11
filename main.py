import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from ui_main import Ui_MainWindow
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Knowledge On The Go')

        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggle_menu(self, 250, True))

        # PAGE 1 - Dictionary
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2 - Wikipedia
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3 - Message-Server
        self.ui.btn_page_3.clicked.connect(lambda: self.server())

        # PAGE 4 - Message-Client
        self.ui.btn_page_4.clicked.connect(lambda: self.client())

    def server(self):
        print()
        print()
        import server

    def client(self):
        print()
        print()
        import client



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
