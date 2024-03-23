# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74075079/attributeerror-qwidget-object-has-no-attribute-tk-did-you-mean-tr-pyqt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy import *
    _l_(597883)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import *
    _l_(597885)

except ImportError:
    pass
try:
    from PyQt5.QtCore import *
    _l_(597887)

except ImportError:
    pass
try:
    from PyQt5.QtGui import *
    _l_(597889)

except ImportError:
    pass
try:
    from tkinter.messagebox import *
    _l_(597891)

except ImportError:
    pass
try:
    import sympy
    _l_(597893)

except ImportError:
    pass
try:
    import sys
    _l_(597895)

except ImportError:
    pass
try:
    from tkinter import Canvas
    _l_(597897)

except ImportError:
    pass
try:
    from untitled import *
    _l_(597899)

except ImportError:
    pass



class canvastrying(_n_(597900, "QMainWindow", lambda: QMainWindow)):
    _l_(597916)

    def __init__(self) -> None:
        _l_(597915)

        _c_(597903, _a_(597902, _n_(597901, "super", lambda: super)(), "__init__"))
        _l_(597904)
        
        _n_(597905, "self", lambda: self).ui = _c_(597907, _n_(597906, "Ui_MainWindow", lambda: Ui_MainWindow))
        _l_(597908)
        _c_(597913, _a_(597911, _a_(597910, _n_(597909, "self", lambda: self), "ui"), "setupUi"), _n_(597912, "self", lambda: self))
        _l_(597914)
if _n_(597917, "__name__", lambda: __name__) == "__main__":
    _l_(597933)

    app = _c_(597921, _n_(597918, "QApplication", lambda: QApplication), _a_(597920, _n_(597919, "sys", lambda: sys), "argv"))
    _l_(597922)
    window = _c_(597924, _n_(597923, "canvastrying", lambda: canvastrying))
    _l_(597925)
    _c_(597931, _a_(597927, _n_(597926, "sys", lambda: sys), "exit"), _c_(597930, _a_(597929, _n_(597928, "app", lambda: app), "exec_")))
    _l_(597932)