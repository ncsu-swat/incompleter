# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61168911/exception-error-python-unhandled-attributeerror-qlineedit-object-has-no-attr
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ultronhouse11\Documents\Eric6\collageApp\ui\demo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    _l_(398355)

except ImportError:
    pass


class Ui_MainWindow(_n_(398356, "object", lambda: object)):
    _l_(398523)

    def setupUi(self, MainWindow):
        _l_(398483)

        _c_(398359, _a_(398358, _n_(398357, "MainWindow", lambda: MainWindow), "setObjectName"), "MainWindow")
        _l_(398360)
        _c_(398363, _a_(398362, _n_(398361, "MainWindow", lambda: MainWindow), "resize"), 800, 600)
        _l_(398364)
        _n_(398365, "self", lambda: self).centralWidget = _c_(398369, _a_(398367, _n_(398366, "QtWidgets", lambda: QtWidgets), "QWidget"), _n_(398368, "MainWindow", lambda: MainWindow))
        _l_(398370)
        _c_(398374, _a_(398373, _a_(398372, _n_(398371, "self", lambda: self), "centralWidget"), "setObjectName"), "centralWidget")
        _l_(398375)
        _n_(398376, "self", lambda: self).btn = _c_(398381, _a_(398378, _n_(398377, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(398380, _n_(398379, "self", lambda: self), "centralWidget"))
        _l_(398382)
        _c_(398389, _a_(398385, _a_(398384, _n_(398383, "self", lambda: self), "btn"), "setGeometry"), _c_(398388, _a_(398387, _n_(398386, "QtCore", lambda: QtCore), "QRect"), 290, 190, 75, 23))
        _l_(398390)
        _c_(398394, _a_(398393, _a_(398392, _n_(398391, "self", lambda: self), "btn"), "setObjectName"), "btn")
        _l_(398395)
        _n_(398396, "self", lambda: self).var = _c_(398401, _a_(398398, _n_(398397, "QtWidgets", lambda: QtWidgets), "QLineEdit"), _a_(398400, _n_(398399, "self", lambda: self), "centralWidget"))
        _l_(398402)
        _c_(398409, _a_(398405, _a_(398404, _n_(398403, "self", lambda: self), "var"), "setGeometry"), _c_(398408, _a_(398407, _n_(398406, "QtCore", lambda: QtCore), "QRect"), 270, 160, 113, 20))
        _l_(398410)
        _c_(398414, _a_(398413, _a_(398412, _n_(398411, "self", lambda: self), "var"), "setObjectName"), "var")
        _l_(398415)
        _n_(398416, "self", lambda: self).show = _c_(398421, _a_(398418, _n_(398417, "QtWidgets", lambda: QtWidgets), "QLabel"), _a_(398420, _n_(398419, "self", lambda: self), "centralWidget"))
        _l_(398422)
        _c_(398429, _a_(398425, _a_(398424, _n_(398423, "self", lambda: self), "show"), "setGeometry"), _c_(398428, _a_(398427, _n_(398426, "QtCore", lambda: QtCore), "QRect"), 230, 260, 241, 41))
        _l_(398430)
        font = _c_(398433, _a_(398432, _n_(398431, "QtGui", lambda: QtGui), "QFont"))
        _l_(398434)
        _c_(398437, _a_(398436, _n_(398435, "font", lambda: font), "setPointSize"), 22)
        _l_(398438)
        _c_(398441, _a_(398440, _n_(398439, "font", lambda: font), "setBold"), True)
        _l_(398442)
        _c_(398445, _a_(398444, _n_(398443, "font", lambda: font), "setWeight"), 75)
        _l_(398446)
        _c_(398451, _a_(398449, _a_(398448, _n_(398447, "self", lambda: self), "show"), "setFont"), _n_(398450, "font", lambda: font))
        _l_(398452)
        _c_(398456, _a_(398455, _a_(398454, _n_(398453, "self", lambda: self), "show"), "setObjectName"), "show")
        _l_(398457)
        _c_(398462, _a_(398459, _n_(398458, "MainWindow", lambda: MainWindow), "setCentralWidget"), _a_(398461, _n_(398460, "self", lambda: self), "centralWidget"))
        _l_(398463)

        _c_(398467, _a_(398465, _n_(398464, "self", lambda: self), "retranslateUi"), _n_(398466, "MainWindow", lambda: MainWindow))
        _l_(398468)
        _c_(398473, _a_(398471, _a_(398470, _n_(398469, "QtCore", lambda: QtCore), "QMetaObject"), "connectSlotsByName"), _n_(398472, "MainWindow", lambda: MainWindow))
        _l_(398474)
        _c_(398481, _a_(398478, _a_(398477, _a_(398476, _n_(398475, "self", lambda: self), "btn"), "clicked"), "connect"), _a_(398480, _n_(398479, "self", lambda: self), "showDB"))
        _l_(398482)

    def retranslateUi(self, MainWindow):
        _l_(398508)

        _translate = _a_(398486, _a_(398485, _n_(398484, "QtCore", lambda: QtCore), "QCoreApplication"), "translate")
        _l_(398487)
        _c_(398492, _a_(398489, _n_(398488, "MainWindow", lambda: MainWindow), "setWindowTitle"), _c_(398491, _n_(398490, "_translate", lambda: _translate), "MainWindow", "MainWindow"))
        _l_(398493)
        _c_(398499, _a_(398496, _a_(398495, _n_(398494, "self", lambda: self), "btn"), "setText"), _c_(398498, _n_(398497, "_translate", lambda: _translate), "MainWindow", "PushButton"))
        _l_(398500)
        _c_(398506, _a_(398503, _a_(398502, _n_(398501, "self", lambda: self), "show"), "setText"), _c_(398505, _n_(398504, "_translate", lambda: _translate), "MainWindow", "TextLabel"))
        _l_(398507)

    def showDB(self):
        _l_(398522)

        _n_(398509, "self", lambda: self).value=_c_(398513, _a_(398512, _a_(398511, _n_(398510, "self", lambda: self), "var"), "get"))
        _l_(398514)
        _c_(398520, _a_(398517, _a_(398516, _n_(398515, "self", lambda: self), "show"), "setText"), _a_(398519, _n_(398518, "self", lambda: self), "value"))
        _l_(398521)


if _n_(398524, "__name__", lambda: __name__) == "__main__":
    _l_(398556)

    try:
        import sys
        _l_(398526)

    except ImportError:
        pass
    app = _c_(398531, _a_(398528, _n_(398527, "QtWidgets", lambda: QtWidgets), "QApplication"), _a_(398530, _n_(398529, "sys", lambda: sys), "argv"))
    _l_(398532)
    MainWindow = _c_(398535, _a_(398534, _n_(398533, "QtWidgets", lambda: QtWidgets), "QMainWindow"))
    _l_(398536)
    ui = _c_(398538, _n_(398537, "Ui_MainWindow", lambda: Ui_MainWindow))
    _l_(398539)
    _c_(398543, _a_(398541, _n_(398540, "ui", lambda: ui), "setupUi"), _n_(398542, "MainWindow", lambda: MainWindow))
    _l_(398544)
    _c_(398547, _a_(398546, _n_(398545, "MainWindow", lambda: MainWindow), "show"))
    _l_(398548)
    _c_(398554, _a_(398550, _n_(398549, "sys", lambda: sys), "exit"), _c_(398553, _a_(398552, _n_(398551, "app", lambda: app), "exec_")))
    _l_(398555)