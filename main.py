from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_CarveBackground import Ui_CarveBackground


def main():
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_CarveBackground()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()




if __name__ == "__main__":
    main()