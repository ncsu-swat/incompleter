# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74075079/attributeerror-qwidget-object-has-no-attribute-tk-did-you-mean-tr-pyqt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    _l_(608726)

except ImportError:
    pass


class Ui_MainWindow(_n_(608727, "object", lambda: object)):
    _l_(608842)

    def setupUi(self, MainWindow):
        _l_(608830)

        _c_(608730, _a_(608729, _n_(608728, "MainWindow", lambda: MainWindow), "setObjectName"), "MainWindow")
        _l_(608731)
        _c_(608734, _a_(608733, _n_(608732, "MainWindow", lambda: MainWindow), "resize"), 318, 325)
        _l_(608735)
        _n_(608736, "self", lambda: self).centralwidget = _c_(608740, _a_(608738, _n_(608737, "QtWidgets", lambda: QtWidgets), "QWidget"), _n_(608739, "MainWindow", lambda: MainWindow))
        _l_(608741)
        _c_(608745, _a_(608744, _a_(608743, _n_(608742, "self", lambda: self), "centralwidget"), "setObjectName"), "centralwidget")
        _l_(608746)
        _n_(608747, "self", lambda: self).widget = _c_(608751, _n_(608748, "Canvas", lambda: Canvas), _a_(608750, _n_(608749, "self", lambda: self), "centralwidget"))
        _l_(608752)
        _c_(608759, _a_(608755, _a_(608754, _n_(608753, "self", lambda: self), "widget"), "setGeometry"), _c_(608758, _a_(608757, _n_(608756, "QtCore", lambda: QtCore), "QRect"), 10, 20, 291, 231))
        _l_(608760)
        _c_(608764, _a_(608763, _a_(608762, _n_(608761, "self", lambda: self), "widget"), "setStyleSheet"), "background-color: green;")
        _l_(608765)
        _c_(608769, _a_(608768, _a_(608767, _n_(608766, "self", lambda: self), "widget"), "setObjectName"), "widget")
        _l_(608770)
        _c_(608775, _a_(608772, _n_(608771, "MainWindow", lambda: MainWindow), "setCentralWidget"), _a_(608774, _n_(608773, "self", lambda: self), "centralwidget"))
        _l_(608776)
        _n_(608777, "self", lambda: self).menubar = _c_(608781, _a_(608779, _n_(608778, "QtWidgets", lambda: QtWidgets), "QMenuBar"), _n_(608780, "MainWindow", lambda: MainWindow))
        _l_(608782)
        _c_(608789, _a_(608785, _a_(608784, _n_(608783, "self", lambda: self), "menubar"), "setGeometry"), _c_(608788, _a_(608787, _n_(608786, "QtCore", lambda: QtCore), "QRect"), 0, 0, 318, 21))
        _l_(608790)
        _c_(608794, _a_(608793, _a_(608792, _n_(608791, "self", lambda: self), "menubar"), "setObjectName"), "menubar")
        _l_(608795)
        _c_(608800, _a_(608797, _n_(608796, "MainWindow", lambda: MainWindow), "setMenuBar"), _a_(608799, _n_(608798, "self", lambda: self), "menubar"))
        _l_(608801)
        _n_(608802, "self", lambda: self).statusbar = _c_(608806, _a_(608804, _n_(608803, "QtWidgets", lambda: QtWidgets), "QStatusBar"), _n_(608805, "MainWindow", lambda: MainWindow))
        _l_(608807)
        _c_(608811, _a_(608810, _a_(608809, _n_(608808, "self", lambda: self), "statusbar"), "setObjectName"), "statusbar")
        _l_(608812)
        _c_(608817, _a_(608814, _n_(608813, "MainWindow", lambda: MainWindow), "setStatusBar"), _a_(608816, _n_(608815, "self", lambda: self), "statusbar"))
        _l_(608818)

        _c_(608822, _a_(608820, _n_(608819, "self", lambda: self), "retranslateUi"), _n_(608821, "MainWindow", lambda: MainWindow))
        _l_(608823)
        _c_(608828, _a_(608826, _a_(608825, _n_(608824, "QtCore", lambda: QtCore), "QMetaObject"), "connectSlotsByName"), _n_(608827, "MainWindow", lambda: MainWindow))
        _l_(608829)

    def retranslateUi(self, MainWindow):
        _l_(608841)

        _translate = _a_(608833, _a_(608832, _n_(608831, "QtCore", lambda: QtCore), "QCoreApplication"), "translate")
        _l_(608834)
        _c_(608839, _a_(608836, _n_(608835, "MainWindow", lambda: MainWindow), "setWindowTitle"), _c_(608838, _n_(608837, "_translate", lambda: _translate), "MainWindow", "MainWindow"))
        _l_(608840)
try:
    from tkinter import Canvas
    _l_(608844)

except ImportError:
    pass