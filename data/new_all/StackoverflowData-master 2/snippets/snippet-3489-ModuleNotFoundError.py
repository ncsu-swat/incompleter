#Source: https://stackoverflow.com/questions/73542588/typeerror-argument-1-has-unexpected-type-qpushbutton
from PyQt5 import QtCore, QtGui, QtWidgets
from testGui import Ui_Test

class Ui_PragrammingGUI(object):
    def open_test_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Test()
        self.ui.setupUi(self.window)
        self.ui.get_all_serials()
        self.window.show()

    def setupUi(self, PragrammingGUI):
        PragrammingGUI.setObjectName("PragrammingGUI")
        PragrammingGUI.resize(237, 177)

        self.centralwidget = QtWidgets.QWidget(PragrammingGUI)
        self.centralwidget.setObjectName("centralwidget")
    
        self.test_2 = QtWidgets.QPushButton(self.centralwidget)
        self.test_2.setGeometry(QtCore.QRect(60, 100, 121, 31))
        self.test_2.setObjectName("test_2")
        self.test_2.clicked.connect(self.open_test_window)

        PragrammingGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PragrammingGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 237, 20))
        self.menubar.setObjectName("menubar")

        PragrammingGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PragrammingGUI)
        self.statusbar.setObjectName("statusbar")
        PragrammingGUI.setStatusBar(self.statusbar)

        self.retranslateUi(PragrammingGUI)
        QtCore.QMetaObject.connectSlotsByName(PragrammingGUI)

    def retranslateUi(self, PragrammingGUI):
        _translate = QtCore.QCoreApplication.translate
        PragrammingGUI.setWindowTitle(_translate("PragrammingGUI", "Programming"))
        self.test_2.setText(_translate("PragrammingGUI", "TEST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PragrammingGUI = QtWidgets.QMainWindow()
    ui = Ui_PragrammingGUI()
    ui.setupUi(PragrammingGUI)
    PragrammingGUI.show()
    sys.exit(app.exec_())