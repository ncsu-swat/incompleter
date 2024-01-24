# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42272289/attributeerror-mymainwindow-object-has-no-attribute-pushbutton
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(414409)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
    _l_(414411)

except ImportError:
    pass
try:
    from PyQt5.QtCore import Qt, QEvent, QObject
    _l_(414413)

except ImportError:
    pass
try:
    from ui_main import Ui_MainWindow
    _l_(414415)

except ImportError:
    pass


class MyMainWindow(_n_(414416, "QMainWindow", lambda: QMainWindow), _n_(414417, "Ui_MainWindow", lambda: Ui_MainWindow)):
    _l_(414488)

    def __init__(self, parent=None):
        _l_(414448)

        _c_(414423, _a_(414421, _n_(414418, "super", lambda: super)(_n_(414419, "MyMainWindow", lambda: MyMainWindow), _n_(414420, "self", lambda: self)), "__init__"), _n_(414422, "parent", lambda: parent))
        _l_(414424)
        _c_(414428, _a_(414426, _n_(414425, "qApp", lambda: qApp), "installEventFilter"), _n_(414427, "self", lambda: self))
        _l_(414429)
        _c_(414437, _a_(414433, _a_(414432, _a_(414431, _n_(414430, "self", lambda: self), "pushButton"), "clicked"), "connect"), _c_(414436, _a_(414435, _n_(414434, "self", lambda: self), "clickButton"))) #here is where the issue is occurs
        _l_(414438) #here is where the issue is occurs
        _c_(414441, _a_(414440, _n_(414439, "self", lambda: self), "show"))
        _l_(414442)
        _c_(414446, _a_(414444, _n_(414443, "self", lambda: self), "setupUi"), _n_(414445, "self", lambda: self))
        _l_(414447)

    def eventFilter(self, obj, event):
        _l_(414473)

        if _c_(414451, _a_(414450, _n_(414449, "event", lambda: event), "type")) == _a_(414453, _n_(414452, "QEvent", lambda: QEvent), "KeyPress"):
            _l_(414464)

            if _c_(414456, _a_(414455, _n_(414454, "event", lambda: event), "key")) == _a_(414458, _n_(414457, "Qt", lambda: Qt), "Key_Escape"):
                _l_(414463)

                _c_(414461, _a_(414460, _n_(414459, "self", lambda: self), "close"))
                _l_(414462)
        aux = _c_(414471, _a_(414468, _n_(414465, "super", lambda: super)(_n_(414466, "MyMainWindow", lambda: MyMainWindow), _n_(414467, "self", lambda: self)), "eventFilter"), _n_(414469, "obj", lambda: obj), _n_(414470, "event", lambda: event))
        _l_(414472)
        return aux

    def clickButton(self):
        _l_(414487)

        sender = _c_(414476, _a_(414475, _n_(414474, "self", lambda: self), "sender"))
        _l_(414477)
        _c_(414485, _a_(414481, _c_(414480, _a_(414479, _n_(414478, "self", lambda: self), "statusbar")), "showMessage"), _c_(414484, _a_(414483, _n_(414482, "sender", lambda: sender), "text")) + ' was pressed')
        _l_(414486)

if _n_(414489, "__name__", lambda: __name__) == '__main__':
    _l_(414508)

    app = _c_(414493, _n_(414490, "QApplication", lambda: QApplication), _a_(414492, _n_(414491, "sys", lambda: sys), "argv"))
    _l_(414494)
    win = _c_(414496, _n_(414495, "MyMainWindow", lambda: MyMainWindow))
    _l_(414497)
    test = _c_(414499, _n_(414498, "TestClass", lambda: TestClass))
    _l_(414500)
    _c_(414506, _a_(414502, _n_(414501, "sys", lambda: sys), "exit"), _c_(414505, _a_(414504, _n_(414503, "app", lambda: app), "exec_")))
    _l_(414507)