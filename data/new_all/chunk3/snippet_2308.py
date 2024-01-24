# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52345457/pyqt4-problems-with-resorce-system-typeerror-qregisterresourcedata
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(536916)

except ImportError:
    pass
try:
    from PyQt4 import QtCore, QtGui, uic
    _l_(536918)

except ImportError:
    pass
try:
    from PyQt4.QtCore import *
    _l_(536920)

except ImportError:
    pass
try:
    from PyQt4.QtGui import *
    _l_(536922)

except ImportError:
    pass

mainwindow = _c_(536925, _a_(536924, _n_(536923, "uic", lambda: uic), "loadUiType"), "mainmenu2.ui")[0] #load the UI
_l_(536926) #load the UI
class Mainmenu(_a_(536928, _n_(536927, "QtGui", lambda: QtGui), "QMainWindow"), _n_(536929, "mainwindow", lambda: mainwindow)):
    _l_(536943)

    def __init__(self, parent=None):
        _l_(536942)

        _c_(536935, _a_(536933, _n_(536930, "super", lambda: super)(_n_(536931, "Mainmenu", lambda: Mainmenu), _n_(536932, "self", lambda: self)), "__init__"), _n_(536934, "parent", lambda: parent))
        _l_(536936)
        _c_(536940, _a_(536938, _n_(536937, "self", lambda: self), "setupUi"), _n_(536939, "self", lambda: self))
        _l_(536941)

app = _c_(536948, _a_(536945, _n_(536944, "QtGui", lambda: QtGui), "QApplication"), _a_(536947, _n_(536946, "sys", lambda: sys), "argv"))
_l_(536949)
mainwindow = _n_(536950, "Mainmenu", lambda: Mainmenu)
_l_(536951)
#aboutwindow = About_us_page(None)
_c_(536954, _a_(536953, _n_(536952, "mainwindow", lambda: mainwindow), "show"))
_l_(536955)
_c_(536958, _a_(536957, _n_(536956, "app", lambda: app), "exec_"))
_l_(536959)