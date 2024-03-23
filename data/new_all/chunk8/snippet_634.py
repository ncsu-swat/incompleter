# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39133568/pyqt5-builtins-attributeerror-qdialog-object-has-no-attribute-setcentralwid
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(399783)

except ImportError:
    pass
try:
    from PyQt5 import QtWidgets, QtCore, QtGui
    _l_(399785)

except ImportError:
    pass
try:
    from testing1 import Ui_MainWindow
    _l_(399787)

except ImportError:
    pass

class myprog(_n_(399788, "Ui_MainWindow", lambda: Ui_MainWindow)):
    _l_(399800)

    def __init__ (self, dialog):
        _l_(399799)

        _c_(399792, _a_(399790, _n_(399789, "Ui_MainWindow", lambda: Ui_MainWindow), "__init__"), _n_(399791, "self", lambda: self))
        _l_(399793)
        _c_(399797, _a_(399795, _n_(399794, "self", lambda: self), "setupUi"), _n_(399796, "dialog", lambda: dialog))
        _l_(399798)


if _n_(399801, "__name__", lambda: __name__) == '__main__':
    _l_(399827)

    app = _c_(399806, _a_(399803, _n_(399802, "QtWidgets", lambda: QtWidgets), "QApplication"), _a_(399805, _n_(399804, "sys", lambda: sys), "argv"))
    _l_(399807)
    dialog = _c_(399810, _a_(399809, _n_(399808, "QtWidgets", lambda: QtWidgets), "QDialog"))
    _l_(399811)

    test1 = _c_(399814, _n_(399812, "myprog", lambda: myprog), _n_(399813, "dialog", lambda: dialog))
    _l_(399815)
    _c_(399818, _a_(399817, _n_(399816, "dialog", lambda: dialog), "show"))
    _l_(399819)
    _c_(399825, _a_(399821, _n_(399820, "sys", lambda: sys), "exit"), _c_(399824, _a_(399823, _n_(399822, "app", lambda: app), "exec_")))
    _l_(399826)