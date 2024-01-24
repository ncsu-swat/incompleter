# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50712783/pyqt5-how-to-display-list-in-qmessagebox-typeerror-argument-3-has-unexpected
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(431598)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
    _l_(431600)

except ImportError:
    pass
try:
    from PyQt5.QtGui import QIcon
    _l_(431602)

except ImportError:
    pass
try:
    from PyQt5.QtCore import pyqtSlot
    _l_(431604)

except ImportError:
    pass

class App(_n_(431605, "QMainWindow", lambda: QMainWindow)):
    _l_(431717)


    def __init__(self):
        _l_(431624)

        _c_(431608, _a_(431607, _n_(431606, "super", lambda: super)(), "__init__"))
        _l_(431609)
        _n_(431610, "self", lambda: self).title = 'List manipulation'
        _l_(431611)
        _n_(431612, "self", lambda: self).left = 10
        _l_(431613)
        _n_(431614, "self", lambda: self).top = 10
        _l_(431615)
        _n_(431616, "self", lambda: self).width = 325
        _l_(431617)
        _n_(431618, "self", lambda: self).height = 300
        _l_(431619)
        _c_(431622, _a_(431621, _n_(431620, "self", lambda: self), "initUI"))
        _l_(431623)

    def initUI(self):
        _l_(431680)

        _c_(431629, _a_(431626, _n_(431625, "self", lambda: self), "setWindowTitle"), _a_(431628, _n_(431627, "self", lambda: self), "title"))
        _l_(431630)
        _c_(431641, _a_(431632, _n_(431631, "self", lambda: self), "setGeometry"), _a_(431634, _n_(431633, "self", lambda: self), "left"), _a_(431636, _n_(431635, "self", lambda: self), "top"), _a_(431638, _n_(431637, "self", lambda: self), "width"), _a_(431640, _n_(431639, "self", lambda: self), "height"))
        _l_(431642)

        # Create textbox
        _n_(431643, "self", lambda: self).textbox = _c_(431646, _n_(431644, "QLineEdit", lambda: QLineEdit), _n_(431645, "self", lambda: self))
        _l_(431647)
        _c_(431651, _a_(431650, _a_(431649, _n_(431648, "self", lambda: self), "textbox"), "move"), 20, 20)
        _l_(431652)
        _c_(431656, _a_(431655, _a_(431654, _n_(431653, "self", lambda: self), "textbox"), "resize"), 280, 200)
        _l_(431657)

        # Create a button in the window
        _n_(431658, "self", lambda: self).button = _c_(431661, _n_(431659, "QPushButton", lambda: QPushButton), 'Show text', _n_(431660, "self", lambda: self))
        _l_(431662)
        _c_(431666, _a_(431665, _a_(431664, _n_(431663, "self", lambda: self), "button"), "move"), 20, 230)
        _l_(431667)

        # connect button to function on_click
        _c_(431674, _a_(431671, _a_(431670, _a_(431669, _n_(431668, "self", lambda: self), "button"), "clicked"), "connect"), _a_(431673, _n_(431672, "self", lambda: self), "on_click"))
        _l_(431675)
        _c_(431678, _a_(431677, _n_(431676, "self", lambda: self), "show"))
        _l_(431679)

    @_c_(431682, _n_(431681, "pyqtSlot", lambda: pyqtSlot))
    def on_click(self):
        _l_(431704)

        textboxValue = _c_(431686, _a_(431685, _a_(431684, _n_(431683, "self", lambda: self), "textbox"), "text"))
        _l_(431687)
        xlist = _c_(431690, _a_(431689, _n_(431688, "textboxValue", lambda: textboxValue), "splitlines"))
        _l_(431691)
        xlist_final=[]
        _l_(431692)
        for xitem in _n_(431693, "xlist", lambda: xlist):
            _l_(431703)

            if _c_(431696, _a_(431695, _n_(431694, "xitem", lambda: xitem), "find"), "abc") != -1:
                _l_(431702)

                _c_(431700, _a_(431698, _n_(431697, "xlist_final", lambda: xlist_final), "append"), _n_(431699, "xitem", lambda: xitem))
                _l_(431701)
    _c_(431711, _a_(431706, _n_(431705, "QMessageBox", lambda: QMessageBox), "question"), self, 'List manipulation', xlist_final, _a_(431708, _n_(431707, "QMessageBox", lambda: QMessageBox), "Ok"), _a_(431710, _n_(431709, "QMessageBox", lambda: QMessageBox), "Ok"))
    _l_(431712)
    _c_(431715, _a_(431714, _a_(431713, self, "textbox"), "setText"), "")
    _l_(431716)


if _n_(431718, "__name__", lambda: __name__) == '__main__':
    _l_(431734)

    app = _c_(431722, _n_(431719, "QApplication", lambda: QApplication), _a_(431721, _n_(431720, "sys", lambda: sys), "argv"))
    _l_(431723)
    ex = _c_(431725, _n_(431724, "App", lambda: App))
    _l_(431726)
    _c_(431732, _a_(431728, _n_(431727, "sys", lambda: sys), "exit"), _c_(431731, _a_(431730, _n_(431729, "app", lambda: app), "exec_")))
    _l_(431733)