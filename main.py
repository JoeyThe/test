import sys
from PySide6 import QtWidgets

from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.magic)

    def magic(self):
        if self.radioButton.isChecked():
            self.changeTextEditTextColor("red")
            self.textEdit.append("Michael Gay in red")
        elif self.radioButton_2.isChecked():
            self.changeTextEditTextColor("green")
            self.textEdit.append("Michael Gay in green")
        elif self.radioButton_3.isChecked():
            self.changeTextEditTextColor("blue")
            self.textEdit.append("Michael Gay in blue")
        else:
            self.changeTextEditTextColor("black")
            self.textEdit.append("Michael Gay")

    def changeTextEditTextColor(self, color):
        self.textEdit.setTextColor(f"{color}")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
