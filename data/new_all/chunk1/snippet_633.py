# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39133568/pyqt5-builtins-attributeerror-qdialog-object-has-no-attribute-setcentralwid
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    _l_(391702)

except ImportError:
    pass

class Ui_MainWindow(_n_(391703, "object", lambda: object)):
    _l_(391821)

    def setupUi(self, MainWindow):
        _l_(391802)

        _c_(391706, _a_(391705, _n_(391704, "MainWindow", lambda: MainWindow), "setObjectName"), "MainWindow")
        _l_(391707)
        _c_(391710, _a_(391709, _n_(391708, "MainWindow", lambda: MainWindow), "resize"), 800, 600)
        _l_(391711)
        _n_(391712, "self", lambda: self).centralwidget = _c_(391716, _a_(391714, _n_(391713, "QtWidgets", lambda: QtWidgets), "QWidget"), _n_(391715, "MainWindow", lambda: MainWindow))
        _l_(391717)
        _c_(391721, _a_(391720, _a_(391719, _n_(391718, "self", lambda: self), "centralwidget"), "setObjectName"), "centralwidget")
        _l_(391722)
        _n_(391723, "self", lambda: self).pushButton = _c_(391728, _a_(391725, _n_(391724, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(391727, _n_(391726, "self", lambda: self), "centralwidget"))
        _l_(391729)
        _c_(391736, _a_(391732, _a_(391731, _n_(391730, "self", lambda: self), "pushButton"), "setGeometry"), _c_(391735, _a_(391734, _n_(391733, "QtCore", lambda: QtCore), "QRect"), 380, 180, 112, 34))
        _l_(391737)
        _c_(391741, _a_(391740, _a_(391739, _n_(391738, "self", lambda: self), "pushButton"), "setObjectName"), "pushButton")
        _l_(391742)
        _c_(391747, _a_(391744, _n_(391743, "MainWindow", lambda: MainWindow), "setCentralWidget"), _a_(391746, _n_(391745, "self", lambda: self), "centralwidget"))
        _l_(391748)
        _n_(391749, "self", lambda: self).menubar = _c_(391753, _a_(391751, _n_(391750, "QtWidgets", lambda: QtWidgets), "QMenuBar"), _n_(391752, "MainWindow", lambda: MainWindow))
        _l_(391754)
        _c_(391761, _a_(391757, _a_(391756, _n_(391755, "self", lambda: self), "menubar"), "setGeometry"), _c_(391760, _a_(391759, _n_(391758, "QtCore", lambda: QtCore), "QRect"), 0, 0, 800, 31))
        _l_(391762)
        _c_(391766, _a_(391765, _a_(391764, _n_(391763, "self", lambda: self), "menubar"), "setObjectName"), "menubar")
        _l_(391767)
        _c_(391772, _a_(391769, _n_(391768, "MainWindow", lambda: MainWindow), "setMenuBar"), _a_(391771, _n_(391770, "self", lambda: self), "menubar"))
        _l_(391773)
        _n_(391774, "self", lambda: self).statusbar = _c_(391778, _a_(391776, _n_(391775, "QtWidgets", lambda: QtWidgets), "QStatusBar"), _n_(391777, "MainWindow", lambda: MainWindow))
        _l_(391779)
        _c_(391783, _a_(391782, _a_(391781, _n_(391780, "self", lambda: self), "statusbar"), "setObjectName"), "statusbar")
        _l_(391784)
        _c_(391789, _a_(391786, _n_(391785, "MainWindow", lambda: MainWindow), "setStatusBar"), _a_(391788, _n_(391787, "self", lambda: self), "statusbar"))
        _l_(391790)

        _c_(391794, _a_(391792, _n_(391791, "self", lambda: self), "retranslateUi"), _n_(391793, "MainWindow", lambda: MainWindow))
        _l_(391795)
        _c_(391800, _a_(391798, _a_(391797, _n_(391796, "QtCore", lambda: QtCore), "QMetaObject"), "connectSlotsByName"), _n_(391799, "MainWindow", lambda: MainWindow))
        _l_(391801)

    def retranslateUi(self, MainWindow):
        _l_(391820)

        _translate = _a_(391805, _a_(391804, _n_(391803, "QtCore", lambda: QtCore), "QCoreApplication"), "translate")
        _l_(391806)
        _c_(391811, _a_(391808, _n_(391807, "MainWindow", lambda: MainWindow), "setWindowTitle"), _c_(391810, _n_(391809, "_translate", lambda: _translate), "MainWindow", "MainWindow"))
        _l_(391812)
        _c_(391818, _a_(391815, _a_(391814, _n_(391813, "self", lambda: self), "pushButton"), "setText"), _c_(391817, _n_(391816, "_translate", lambda: _translate), "MainWindow", "PushButton"))
        _l_(391819)


if _n_(391822, "__name__", lambda: __name__) == "__main__":
    _l_(391854)

    try:
        import sys
        _l_(391824)

    except ImportError:
        pass
    app = _c_(391829, _a_(391826, _n_(391825, "QtWidgets", lambda: QtWidgets), "QApplication"), _a_(391828, _n_(391827, "sys", lambda: sys), "argv"))
    _l_(391830)
    MainWindow = _c_(391833, _a_(391832, _n_(391831, "QtWidgets", lambda: QtWidgets), "QMainWindow"))
    _l_(391834)
    ui = _c_(391836, _n_(391835, "Ui_MainWindow", lambda: Ui_MainWindow))
    _l_(391837)
    _c_(391841, _a_(391839, _n_(391838, "ui", lambda: ui), "setupUi"), _n_(391840, "MainWindow", lambda: MainWindow))
    _l_(391842)
    _c_(391845, _a_(391844, _n_(391843, "MainWindow", lambda: MainWindow), "show"))
    _l_(391846)
    _c_(391852, _a_(391848, _n_(391847, "sys", lambda: sys), "exit"), _c_(391851, _a_(391850, _n_(391849, "app", lambda: app), "exec_")))
    _l_(391853)