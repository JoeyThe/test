import sys
from PySide6 import QtWidgets

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.magic)

    def magic(self):
        self.textEdit.append("Michael Gay ")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
