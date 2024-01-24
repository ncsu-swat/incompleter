#Source: https://stackoverflow.com/questions/73542588/typeerror-argument-1-has-unexpected-type-qpushbutton
import sys
import os
from cameraID import CameraID
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(QDialog):

    def browse_file_src(self):
        print('in the function')
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home/qauser/')
        self.lineEdit.setText(file_name[0])

    def get_all_serials(self):
        self.serial = CameraID()
        self.serial.getAllSerial()
        return_list = self.serial.getAllSerial()
        if len(return_list) > 0:
            for i in return_list:
                self.comboBox.addItem(i)
        else:
            self.comboBox.addItem("None")

    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(397, 108)
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 291, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Chose file")

        self.browseBtn = QtWidgets.QPushButton(self.centralwidget)#, clicked=lambda: self.browseBtn)
        self.browseBtn.setGeometry(QtCore.QRect(310, 10, 80, 23))
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.browseBtn)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 51, 21))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 40, 71, 21))
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 40, 80, 23))
        self.pushButton.setObjectName("pushButton")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 40, 181, 23))
        self.comboBox.setObjectName("comboBox")

        Test.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Test)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 20))
        self.menubar.setObjectName("menubar")
        Test.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Test)
        self.statusbar.setObjectName("statusbar")
        Test.setStatusBar(self.statusbar)

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "MainWindow"))
        self.browseBtn.setText(_translate("Test", "Browse"))
        self.radioButton.setText(_translate("Test", "Ok"))
        self.radioButton_2.setText(_translate("Test", "Failed"))
        self.pushButton.setText(_translate("Test", "Start"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test = QtWidgets.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())