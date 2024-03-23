# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73542588/typeerror-argument-1-has-unexpected-type-qpushbutton
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    _l_(612025)

except ImportError:
    pass
try:
    from testGui import Ui_Test
    _l_(612027)

except ImportError:
    pass

class Ui_PragrammingGUI(_n_(612028, "object", lambda: object)):
    _l_(612181)

    def open_test_window(self):
        _l_(612055)

        _n_(612029, "self", lambda: self).window = _c_(612032, _a_(612031, _n_(612030, "QtWidgets", lambda: QtWidgets), "QMainWindow"))
        _l_(612033)
        _n_(612034, "self", lambda: self).ui = _c_(612036, _n_(612035, "Ui_Test", lambda: Ui_Test))
        _l_(612037)
        _c_(612043, _a_(612040, _a_(612039, _n_(612038, "self", lambda: self), "ui"), "setupUi"), _a_(612042, _n_(612041, "self", lambda: self), "window"))
        _l_(612044)
        _c_(612048, _a_(612047, _a_(612046, _n_(612045, "self", lambda: self), "ui"), "get_all_serials"))
        _l_(612049)
        _c_(612053, _a_(612052, _a_(612051, _n_(612050, "self", lambda: self), "window"), "show"))
        _l_(612054)

    def setupUi(self, PragrammingGUI):
        _l_(612162)

        _c_(612058, _a_(612057, _n_(612056, "PragrammingGUI", lambda: PragrammingGUI), "setObjectName"), "PragrammingGUI")
        _l_(612059)
        _c_(612062, _a_(612061, _n_(612060, "PragrammingGUI", lambda: PragrammingGUI), "resize"), 237, 177)
        _l_(612063)

        _n_(612064, "self", lambda: self).centralwidget = _c_(612068, _a_(612066, _n_(612065, "QtWidgets", lambda: QtWidgets), "QWidget"), _n_(612067, "PragrammingGUI", lambda: PragrammingGUI))
        _l_(612069)
        _c_(612073, _a_(612072, _a_(612071, _n_(612070, "self", lambda: self), "centralwidget"), "setObjectName"), "centralwidget")
        _l_(612074)
    
        _n_(612075, "self", lambda: self).test_2 = _c_(612080, _a_(612077, _n_(612076, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(612079, _n_(612078, "self", lambda: self), "centralwidget"))
        _l_(612081)
        _c_(612088, _a_(612084, _a_(612083, _n_(612082, "self", lambda: self), "test_2"), "setGeometry"), _c_(612087, _a_(612086, _n_(612085, "QtCore", lambda: QtCore), "QRect"), 60, 100, 121, 31))
        _l_(612089)
        _c_(612093, _a_(612092, _a_(612091, _n_(612090, "self", lambda: self), "test_2"), "setObjectName"), "test_2")
        _l_(612094)
        _c_(612101, _a_(612098, _a_(612097, _a_(612096, _n_(612095, "self", lambda: self), "test_2"), "clicked"), "connect"), _a_(612100, _n_(612099, "self", lambda: self), "open_test_window"))
        _l_(612102)

        _c_(612107, _a_(612104, _n_(612103, "PragrammingGUI", lambda: PragrammingGUI), "setCentralWidget"), _a_(612106, _n_(612105, "self", lambda: self), "centralwidget"))
        _l_(612108)
        _n_(612109, "self", lambda: self).menubar = _c_(612113, _a_(612111, _n_(612110, "QtWidgets", lambda: QtWidgets), "QMenuBar"), _n_(612112, "PragrammingGUI", lambda: PragrammingGUI))
        _l_(612114)
        _c_(612121, _a_(612117, _a_(612116, _n_(612115, "self", lambda: self), "menubar"), "setGeometry"), _c_(612120, _a_(612119, _n_(612118, "QtCore", lambda: QtCore), "QRect"), 0, 0, 237, 20))
        _l_(612122)
        _c_(612126, _a_(612125, _a_(612124, _n_(612123, "self", lambda: self), "menubar"), "setObjectName"), "menubar")
        _l_(612127)

        _c_(612132, _a_(612129, _n_(612128, "PragrammingGUI", lambda: PragrammingGUI), "setMenuBar"), _a_(612131, _n_(612130, "self", lambda: self), "menubar"))
        _l_(612133)
        _n_(612134, "self", lambda: self).statusbar = _c_(612138, _a_(612136, _n_(612135, "QtWidgets", lambda: QtWidgets), "QStatusBar"), _n_(612137, "PragrammingGUI", lambda: PragrammingGUI))
        _l_(612139)
        _c_(612143, _a_(612142, _a_(612141, _n_(612140, "self", lambda: self), "statusbar"), "setObjectName"), "statusbar")
        _l_(612144)
        _c_(612149, _a_(612146, _n_(612145, "PragrammingGUI", lambda: PragrammingGUI), "setStatusBar"), _a_(612148, _n_(612147, "self", lambda: self), "statusbar"))
        _l_(612150)

        _c_(612154, _a_(612152, _n_(612151, "self", lambda: self), "retranslateUi"), _n_(612153, "PragrammingGUI", lambda: PragrammingGUI))
        _l_(612155)
        _c_(612160, _a_(612158, _a_(612157, _n_(612156, "QtCore", lambda: QtCore), "QMetaObject"), "connectSlotsByName"), _n_(612159, "PragrammingGUI", lambda: PragrammingGUI))
        _l_(612161)

    def retranslateUi(self, PragrammingGUI):
        _l_(612180)

        _translate = _a_(612165, _a_(612164, _n_(612163, "QtCore", lambda: QtCore), "QCoreApplication"), "translate")
        _l_(612166)
        _c_(612171, _a_(612168, _n_(612167, "PragrammingGUI", lambda: PragrammingGUI), "setWindowTitle"), _c_(612170, _n_(612169, "_translate", lambda: _translate), "PragrammingGUI", "Programming"))
        _l_(612172)
        _c_(612178, _a_(612175, _a_(612174, _n_(612173, "self", lambda: self), "test_2"), "setText"), _c_(612177, _n_(612176, "_translate", lambda: _translate), "PragrammingGUI", "TEST"))
        _l_(612179)


if _n_(612182, "__name__", lambda: __name__) == "__main__":
    _l_(612214)

    try:
        import sys
        _l_(612184)

    except ImportError:
        pass
    app = _c_(612189, _a_(612186, _n_(612185, "QtWidgets", lambda: QtWidgets), "QApplication"), _a_(612188, _n_(612187, "sys", lambda: sys), "argv"))
    _l_(612190)
    PragrammingGUI = _c_(612193, _a_(612192, _n_(612191, "QtWidgets", lambda: QtWidgets), "QMainWindow"))
    _l_(612194)
    ui = _c_(612196, _n_(612195, "Ui_PragrammingGUI", lambda: Ui_PragrammingGUI))
    _l_(612197)
    _c_(612201, _a_(612199, _n_(612198, "ui", lambda: ui), "setupUi"), _n_(612200, "PragrammingGUI", lambda: PragrammingGUI))
    _l_(612202)
    _c_(612205, _a_(612204, _n_(612203, "PragrammingGUI", lambda: PragrammingGUI), "show"))
    _l_(612206)
    _c_(612212, _a_(612208, _n_(612207, "sys", lambda: sys), "exit"), _c_(612211, _a_(612210, _n_(612209, "app", lambda: app), "exec_")))
    _l_(612213)