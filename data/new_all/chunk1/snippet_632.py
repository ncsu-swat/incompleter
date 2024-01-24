# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42150905/pyqt5-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(388152)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QBoxLayout
    _l_(388154)

except ImportError:
    pass
try:
    from PyQt5.QtGui import QIcon
    _l_(388156)

except ImportError:
    pass
try:
    from PyQt5.QtCore import pyqtSlot
    _l_(388158)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
    _l_(388160)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QInputDialog, QLineEdit
    _l_(388162)

except ImportError:
    pass


class App(_n_(388163, "QDialog", lambda: QDialog)):
    _l_(388224)


    def __init__(self):
        _l_(388182)

        _c_(388166, _a_(388165, _n_(388164, "super", lambda: super)(), "__init__"))
        _l_(388167)
        _n_(388168, "self", lambda: self).title = "PyQt5 example - pythonspot.com"
        _l_(388169)
        _n_(388170, "self", lambda: self).left = 10
        _l_(388171)
        _n_(388172, "self", lambda: self).right = 10
        _l_(388173)
        _n_(388174, "self", lambda: self).width = 640
        _l_(388175)
        _n_(388176, "self", lambda: self).height = 400
        _l_(388177)
        _c_(388180, _a_(388179, _n_(388178, "self", lambda: self), "initUI"))
        _l_(388181)

    def initUI(self):
        _l_(388213)

        _c_(388187, _a_(388184, _n_(388183, "self", lambda: self), "setWindowTitle"), _a_(388186, _n_(388185, "self", lambda: self), "title"))
        _l_(388188)
        _c_(388199, _a_(388190, _n_(388189, "self", lambda: self), "setGeometry"), _a_(388192, _n_(388191, "self", lambda: self), "left"), _a_(388194, _n_(388193, "self", lambda: self), "top"), _a_(388196, _n_(388195, "self", lambda: self), "width"), _a_(388198, _n_(388197, "self", lambda: self), "height"))
        _l_(388200)

        age = _c_(388203, _a_(388202, _n_(388201, "self", lambda: self), "getAge"))
        _l_(388204)
        _c_(388207, _n_(388205, "print", lambda: print), _n_(388206, "age", lambda: age))
        _l_(388208)

        _c_(388211, _a_(388210, _n_(388209, "self", lambda: self), "show"))
        _l_(388212)

    def getAge(self):
        _l_(388223)

        age, okPressed = _c_(388217, _a_(388215, _n_(388214, "QInputDialog", lambda: QInputDialog), "getInt"), _n_(388216, "self", lambda: self), "Get Integer", "Age:", 18, 16, 130, 1)
        _l_(388218)
        if _n_(388219, "okPressed", lambda: okPressed):
            _l_(388222)

            aux = _n_(388220, "age", lambda: age)
            _l_(388221)
            return aux


if _n_(388225, "__name__", lambda: __name__) == '__main__':
    _l_(388241)

    app = _c_(388229, _n_(388226, "QApplication", lambda: QApplication), _a_(388228, _n_(388227, "sys", lambda: sys), "argv"))
    _l_(388230)
    ex = _c_(388232, _n_(388231, "App", lambda: App))
    _l_(388233)
    _c_(388239, _a_(388235, _n_(388234, "sys", lambda: sys), "exit"), _c_(388238, _a_(388237, _n_(388236, "app", lambda: app), "exec_")))
    _l_(388240)