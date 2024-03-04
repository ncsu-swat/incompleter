#Source: https://stackoverflow.com/questions/42150905/pyqt5-nameerror
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QInputDialog, QLineEdit


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 example - pythonspot.com"
        self.left = 10
        self.right = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        age = self.getAge()
        print(age)

        self.show()

    def getAge(self):
        age, okPressed = QInputDialog.getInt(self, "Get Integer", "Age:", 18, 16, 130, 1)
        if okPressed:
            return age


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())