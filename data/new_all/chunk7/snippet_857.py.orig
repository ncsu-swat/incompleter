#Source: https://stackoverflow.com/questions/61168911/exception-error-python-unhandled-attributeerror-qlineedit-object-has-no-attr
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ultronhouse11\Documents\Eric6\collageApp\ui\demo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn = QtWidgets.QPushButton(self.centralWidget)
        self.btn.setGeometry(QtCore.QRect(290, 190, 75, 23))
        self.btn.setObjectName("btn")
        self.var = QtWidgets.QLineEdit(self.centralWidget)
        self.var.setGeometry(QtCore.QRect(270, 160, 113, 20))
        self.var.setObjectName("var")
        self.show = QtWidgets.QLabel(self.centralWidget)
        self.show.setGeometry(QtCore.QRect(230, 260, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.show.setFont(font)
        self.show.setObjectName("show")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn.clicked.connect(self.showDB)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "PushButton"))
        self.show.setText(_translate("MainWindow", "TextLabel"))

    def showDB(self):
        self.value=self.var.get()
        self.show.setText(self.value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())