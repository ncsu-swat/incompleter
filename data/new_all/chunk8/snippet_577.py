# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42272289/attributeerror-mymainwindow-object-has-no-attribute-pushbutton
    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    _l_(408636)

except ImportError:
    pass

class Ui_MainWindow(_n_(408637, "object", lambda: object)):
    _l_(408896)

    def setupUi(self, MainWindow):
        _l_(408863)

        _c_(408640, _a_(408639, _n_(408638, "MainWindow", lambda: MainWindow), "setObjectName"), "MainWindow")
        _l_(408641)
        _c_(408644, _a_(408643, _n_(408642, "MainWindow", lambda: MainWindow), "resize"), 349, 131)
        _l_(408645)
        _n_(408646, "self", lambda: self).centralwidget = _c_(408650, _a_(408648, _n_(408647, "QtWidgets", lambda: QtWidgets), "QWidget"), _n_(408649, "MainWindow", lambda: MainWindow))
        _l_(408651)
        _c_(408655, _a_(408654, _a_(408653, _n_(408652, "self", lambda: self), "centralwidget"), "setObjectName"), "centralwidget")
        _l_(408656)
        _n_(408657, "self", lambda: self).gridLayout = _c_(408662, _a_(408659, _n_(408658, "QtWidgets", lambda: QtWidgets), "QGridLayout"), _a_(408661, _n_(408660, "self", lambda: self), "centralwidget"))
        _l_(408663)
        _c_(408667, _a_(408666, _a_(408665, _n_(408664, "self", lambda: self), "gridLayout"), "setObjectName"), "gridLayout")
        _l_(408668)
        _n_(408669, "self", lambda: self).formLayout = _c_(408672, _a_(408671, _n_(408670, "QtWidgets", lambda: QtWidgets), "QFormLayout"))
        _l_(408673)
        _c_(408677, _a_(408676, _a_(408675, _n_(408674, "self", lambda: self), "formLayout"), "setObjectName"), "formLayout")
        _l_(408678)
        _n_(408679, "self", lambda: self).lineEdit = _c_(408684, _a_(408681, _n_(408680, "QtWidgets", lambda: QtWidgets), "QLineEdit"), _a_(408683, _n_(408682, "self", lambda: self), "centralwidget"))
        _l_(408685)
        _c_(408695, _a_(408688, _a_(408687, _n_(408686, "self", lambda: self), "lineEdit"), "setAlignment"), _a_(408691, _a_(408690, _n_(408689, "QtCore", lambda: QtCore), "Qt"), "AlignHCenter")|_a_(408694, _a_(408693, _n_(408692, "QtCore", lambda: QtCore), "Qt"), "AlignTop"))
        _l_(408696)
        _c_(408700, _a_(408699, _a_(408698, _n_(408697, "self", lambda: self), "lineEdit"), "setObjectName"), "lineEdit")
        _l_(408701)
        _c_(408710, _a_(408704, _a_(408703, _n_(408702, "self", lambda: self), "formLayout"), "setWidget"), 1, _a_(408707, _a_(408706, _n_(408705, "QtWidgets", lambda: QtWidgets), "QFormLayout"), "SpanningRole"), _a_(408709, _n_(408708, "self", lambda: self), "lineEdit"))
        _l_(408711)
        _n_(408712, "self", lambda: self).label = _c_(408717, _a_(408714, _n_(408713, "QtWidgets", lambda: QtWidgets), "QLabel"), _a_(408716, _n_(408715, "self", lambda: self), "centralwidget"))
        _l_(408718)
        _c_(408725, _a_(408721, _a_(408720, _n_(408719, "self", lambda: self), "label"), "setAlignment"), _a_(408724, _a_(408723, _n_(408722, "QtCore", lambda: QtCore), "Qt"), "AlignCenter"))
        _l_(408726)
        _c_(408730, _a_(408729, _a_(408728, _n_(408727, "self", lambda: self), "label"), "setObjectName"), "label")
        _l_(408731)
        _c_(408740, _a_(408734, _a_(408733, _n_(408732, "self", lambda: self), "formLayout"), "setWidget"), 0, _a_(408737, _a_(408736, _n_(408735, "QtWidgets", lambda: QtWidgets), "QFormLayout"), "SpanningRole"), _a_(408739, _n_(408738, "self", lambda: self), "label"))
        _l_(408741)
        _c_(408747, _a_(408744, _a_(408743, _n_(408742, "self", lambda: self), "gridLayout"), "addLayout"), _a_(408746, _n_(408745, "self", lambda: self), "formLayout"), 0, 0, 1, 1)
        _l_(408748)
        _n_(408749, "self", lambda: self).horizontalLayout = _c_(408752, _a_(408751, _n_(408750, "QtWidgets", lambda: QtWidgets), "QHBoxLayout"))
        _l_(408753)
        _c_(408757, _a_(408756, _a_(408755, _n_(408754, "self", lambda: self), "horizontalLayout"), "setObjectName"), "horizontalLayout")
        _l_(408758)
        _n_(408759, "self", lambda: self).pushButton = _c_(408764, _a_(408761, _n_(408760, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(408763, _n_(408762, "self", lambda: self), "centralwidget"))
        _l_(408765)
        _c_(408769, _a_(408768, _a_(408767, _n_(408766, "self", lambda: self), "pushButton"), "setObjectName"), "pushButton")
        _l_(408770)
        _c_(408776, _a_(408773, _a_(408772, _n_(408771, "self", lambda: self), "horizontalLayout"), "addWidget"), _a_(408775, _n_(408774, "self", lambda: self), "pushButton"))
        _l_(408777)
        _n_(408778, "self", lambda: self).pushButton_2 = _c_(408783, _a_(408780, _n_(408779, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(408782, _n_(408781, "self", lambda: self), "centralwidget"))
        _l_(408784)
        _c_(408788, _a_(408787, _a_(408786, _n_(408785, "self", lambda: self), "pushButton_2"), "setObjectName"), "pushButton_2")
        _l_(408789)
        _c_(408795, _a_(408792, _a_(408791, _n_(408790, "self", lambda: self), "horizontalLayout"), "addWidget"), _a_(408794, _n_(408793, "self", lambda: self), "pushButton_2"))
        _l_(408796)
        _c_(408802, _a_(408799, _a_(408798, _n_(408797, "self", lambda: self), "gridLayout"), "addLayout"), _a_(408801, _n_(408800, "self", lambda: self), "horizontalLayout"), 1, 0, 1, 1)
        _l_(408803)
        _c_(408808, _a_(408805, _n_(408804, "MainWindow", lambda: MainWindow), "setCentralWidget"), _a_(408807, _n_(408806, "self", lambda: self), "centralwidget"))
        _l_(408809)
        _n_(408810, "self", lambda: self).menubar = _c_(408814, _a_(408812, _n_(408811, "QtWidgets", lambda: QtWidgets), "QMenuBar"), _n_(408813, "MainWindow", lambda: MainWindow))
        _l_(408815)
        _c_(408822, _a_(408818, _a_(408817, _n_(408816, "self", lambda: self), "menubar"), "setGeometry"), _c_(408821, _a_(408820, _n_(408819, "QtCore", lambda: QtCore), "QRect"), 0, 0, 349, 21))
        _l_(408823)
        _c_(408827, _a_(408826, _a_(408825, _n_(408824, "self", lambda: self), "menubar"), "setObjectName"), "menubar")
        _l_(408828)
        _c_(408833, _a_(408830, _n_(408829, "MainWindow", lambda: MainWindow), "setMenuBar"), _a_(408832, _n_(408831, "self", lambda: self), "menubar"))
        _l_(408834)
        _n_(408835, "self", lambda: self).statusbar = _c_(408839, _a_(408837, _n_(408836, "QtWidgets", lambda: QtWidgets), "QStatusBar"), _n_(408838, "MainWindow", lambda: MainWindow))
        _l_(408840)
        _c_(408844, _a_(408843, _a_(408842, _n_(408841, "self", lambda: self), "statusbar"), "setObjectName"), "statusbar")
        _l_(408845)
        _c_(408850, _a_(408847, _n_(408846, "MainWindow", lambda: MainWindow), "setStatusBar"), _a_(408849, _n_(408848, "self", lambda: self), "statusbar"))
        _l_(408851)

        _c_(408855, _a_(408853, _n_(408852, "self", lambda: self), "retranslateUi"), _n_(408854, "MainWindow", lambda: MainWindow))
        _l_(408856)
        _c_(408861, _a_(408859, _a_(408858, _n_(408857, "QtCore", lambda: QtCore), "QMetaObject"), "connectSlotsByName"), _n_(408860, "MainWindow", lambda: MainWindow))
        _l_(408862)

    def retranslateUi(self, MainWindow):
        _l_(408895)

        _translate = _a_(408866, _a_(408865, _n_(408864, "QtCore", lambda: QtCore), "QCoreApplication"), "translate")
        _l_(408867)
        _c_(408872, _a_(408869, _n_(408868, "MainWindow", lambda: MainWindow), "setWindowTitle"), _c_(408871, _n_(408870, "_translate", lambda: _translate), "MainWindow", "MainWindow"))
        _l_(408873)
        _c_(408879, _a_(408876, _a_(408875, _n_(408874, "self", lambda: self), "label"), "setText"), _c_(408878, _n_(408877, "_translate", lambda: _translate), "MainWindow", "TextLabel"))
        _l_(408880)
        _c_(408886, _a_(408883, _a_(408882, _n_(408881, "self", lambda: self), "pushButton"), "setText"), _c_(408885, _n_(408884, "_translate", lambda: _translate), "MainWindow", "PushButton"))
        _l_(408887)
        _c_(408893, _a_(408890, _a_(408889, _n_(408888, "self", lambda: self), "pushButton_2"), "setText"), _c_(408892, _n_(408891, "_translate", lambda: _translate), "MainWindow", "PushButton"))
        _l_(408894)


if _n_(408897, "__name__", lambda: __name__) == "__main__":
    _l_(408929)

    try:
        import sys
        _l_(408899)

    except ImportError:
        pass
    app = _c_(408904, _a_(408901, _n_(408900, "QtWidgets", lambda: QtWidgets), "QApplication"), _a_(408903, _n_(408902, "sys", lambda: sys), "argv"))
    _l_(408905)
    MainWindow = _c_(408908, _a_(408907, _n_(408906, "QtWidgets", lambda: QtWidgets), "QMainWindow"))
    _l_(408909)
    ui = _c_(408911, _n_(408910, "Ui_MainWindow", lambda: Ui_MainWindow))
    _l_(408912)
    _c_(408916, _a_(408914, _n_(408913, "ui", lambda: ui), "setupUi"), _n_(408915, "MainWindow", lambda: MainWindow))
    _l_(408917)
    _c_(408920, _a_(408919, _n_(408918, "MainWindow", lambda: MainWindow), "show"))
    _l_(408921)
    _c_(408927, _a_(408923, _n_(408922, "sys", lambda: sys), "exit"), _c_(408926, _a_(408925, _n_(408924, "app", lambda: app), "exec_")))
    _l_(408928)