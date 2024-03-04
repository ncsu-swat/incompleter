#Source: https://stackoverflow.com/questions/39133568/pyqt5-builtins-attributeerror-qdialog-object-has-no-attribute-setcentralwid
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from testing1 import Ui_MainWindow

class myprog(Ui_MainWindow):
    def __init__ (self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    test1 = myprog(dialog)
    dialog.show()
    sys.exit(app.exec_())