# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18831771/pyqt4-signal-attributeerror-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt4.QtCore import *
    _l_(541801)

except ImportError:
    pass
try:
    from PyQt4.QtGui import *
    _l_(541803)

except ImportError:
    pass
try:
    import sys
    _l_(541805)

except ImportError:
    pass

class StringListDlg(_n_(541806, "QDialog", lambda: QDialog)):
    _l_(541860)


    def __init__(self, name, strings, parent=None):
        _l_(541859)

        _c_(541812, _a_(541810, _n_(541807, "super", lambda: super)(_n_(541808, "StringListDlg", lambda: StringListDlg), _n_(541809, "self", lambda: self)), "__init__"), _n_(541811, "parent", lambda: parent))
        _l_(541813)

        _n_(541814, "self", lambda: self).listWidget = _c_(541816, _n_(541815, "QListWidget", lambda: QListWidget))
        _l_(541817)
        _c_(541822, _a_(541820, _a_(541819, _n_(541818, "self", lambda: self), "listWidget"), "addItems"), _n_(541821, "strings", lambda: strings))
        _l_(541823)
        addButton = _c_(541825, _n_(541824, "QPushButton", lambda: QPushButton), "&Add...")
        _l_(541826)

        grid = _c_(541828, _n_(541827, "QGridLayout", lambda: QGridLayout))
        _l_(541829)
        _c_(541834, _a_(541831, _n_(541830, "grid", lambda: grid), "addWidget"), _a_(541833, _n_(541832, "self", lambda: self), "listWidget"), 0, 0, 7, 1)
        _l_(541835)

        _c_(541839, _a_(541837, _n_(541836, "self", lambda: self), "setLayout"), _n_(541838, "grid", lambda: grid))
        _l_(541840)
        _c_(541846, _a_(541842, _n_(541841, "self", lambda: self), "setWindowTitle"), _c_(541845, _a_(541843, "Edit {} List", "format"), _n_(541844, "name", lambda: name)))
        _l_(541847)

        _c_(541855, _a_(541849, _n_(541848, "self", lambda: self), "connect"), _n_(541850, "addButton", lambda: addButton), _c_(541852, _n_(541851, "SIGNAL", lambda: SIGNAL), "clicked()"), _a_(541854, _n_(541853, "self", lambda: self), "add"))
        _l_(541856)

        def add(self):
            _l_(541858)

            pass
            _l_(541857)

if _n_(541861, "__name__", lambda: __name__) == "__main__":
    _l_(541874)

    app = _c_(541865, _n_(541862, "QApplication", lambda: QApplication), _a_(541864, _n_(541863, "sys", lambda: sys), "argv"))
    _l_(541866)
    form = _c_(541868, _n_(541867, "StringListDlg", lambda: StringListDlg), "Fruit", ['apples', 'bananas'])
    _l_(541869)
    _c_(541872, _a_(541871, _n_(541870, "form", lambda: form), "exec_"))
    _l_(541873)