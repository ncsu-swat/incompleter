# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61128279/pyside2-how-to-unassign-current-layout-and-assign-a-new-one-to-a-window-widget
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(647273)

except ImportError:
    pass
try:
    from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QWidget
    _l_(647275)

except ImportError:
    pass
try:
    from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLayout
    _l_(647277)

except ImportError:
    pass

class Window(_n_(647278, "QWidget", lambda: QWidget)):
    _l_(647376)

    def __init__(self):
        _l_(647295)

        _c_(647281, _a_(647280, _n_(647279, "super", lambda: super)(), "__init__"))
        _l_(647282)
        _c_(647285, _a_(647284, _n_(647283, "self", lambda: self), "setWindowTitle"), "Program")
        _l_(647286)
        _c_(647289, _a_(647288, _n_(647287, "self", lambda: self), "setGeometry"), 300, 300, 300, 300)
        _l_(647290)
        _c_(647293, _a_(647292, _n_(647291, "self", lambda: self), "start"))
        _l_(647294)

    def clearLayout(self, layout):
        _l_(647323)

        if _n_(647296, "layout", lambda: layout) is not None:
            _l_(647322)

            while _c_(647299, _a_(647298, _n_(647297, "layout", lambda: layout), "count")):
                _l_(647321)

                item = _c_(647302, _a_(647301, _n_(647300, "layout", lambda: layout), "takeAt"), 0)
                _l_(647303)
                widget = _c_(647306, _a_(647305, _n_(647304, "item", lambda: item), "widget"))
                _l_(647307)
                if _n_(647308, "widget", lambda: widget) is not None:
                    _l_(647320)

                    _c_(647311, _a_(647310, _n_(647309, "widget", lambda: widget), "deleteLater"))
                    _l_(647312)
                else:
                    _c_(647318, _a_(647314, _n_(647313, "self", lambda: self), "clearLayout"), _c_(647317, _a_(647316, _n_(647315, "item", lambda: item), "layout")))
                    _l_(647319)

    def start(self):
        _l_(647350)

        _n_(647324, "self", lambda: self).startbutton = _c_(647326, _n_(647325, "QPushButton", lambda: QPushButton), "Start App")
        _l_(647327)

        layout = _c_(647329, _n_(647328, "QVBoxLayout", lambda: QVBoxLayout))
        _l_(647330)
        _c_(647335, _a_(647332, _n_(647331, "layout", lambda: layout), "addWidget"), _a_(647334, _n_(647333, "self", lambda: self), "startbutton"))
        _l_(647336)

        _c_(647340, _a_(647338, _n_(647337, "self", lambda: self), "setLayout"), _n_(647339, "layout", lambda: layout))
        _l_(647341)

        _c_(647348, _a_(647345, _a_(647344, _a_(647343, _n_(647342, "self", lambda: self), "startbutton"), "clicked"), "connect"), _a_(647347, _n_(647346, "self", lambda: self), "home"))
        _l_(647349)

    def home(self):
        _l_(647375)

        _c_(647355, _a_(647352, _n_(647351, "self", lambda: self), "clearLayout"), _a_(647354, _n_(647353, "self", lambda: self), "layout"))
        _l_(647356)
        _n_(647357, "self", lambda: self).message=_c_(647359, _n_(647358, "QLabel", lambda: QLabel), "Welcome to homepage")
        _l_(647360)
        layout=_c_(647362, _n_(647361, "QVBoxLayout", lambda: QVBoxLayout))
        _l_(647363)
        _c_(647368, _a_(647365, _n_(647364, "layout", lambda: layout), "addWidget"), _a_(647367, _n_(647366, "self", lambda: self), "message"))
        _l_(647369)
        _c_(647373, _a_(647371, _n_(647370, "self", lambda: self), "setLayout"), _n_(647372, "layout", lambda: layout))
        _l_(647374)

if _n_(647377, "__name__", lambda: __name__) == "__main__":
    _l_(647395)

    app = _c_(647379, _n_(647378, "QApplication", lambda: QApplication), [])
    _l_(647380)
    window=_c_(647382, _n_(647381, "Window", lambda: Window))
    _l_(647383)
    _c_(647386, _a_(647385, _n_(647384, "window", lambda: window), "show"))
    _l_(647387)
    _c_(647393, _a_(647389, _n_(647388, "sys", lambda: sys), "exit"), _c_(647392, _a_(647391, _n_(647390, "app", lambda: app), "exec_")))
    _l_(647394)