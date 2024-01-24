# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66488675/pyqt5-error-typeerror-arguments-did-not-match-any-overloaded-call
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(463371)

except ImportError:
    pass
try:
    from PyQt5.QtCore import *
    _l_(463373)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import *
    _l_(463375)

except ImportError:
    pass
try:
    from PyQt5.QtWebEngineWidgets import *
    _l_(463377)

except ImportError:
    pass


class MainWindow(_n_(463378, "QMainWindow", lambda: QMainWindow)):
    _l_(463477)

    def __init__(self):
        _l_(463476)

        _c_(463383, _a_(463382, _n_(463379, "super", lambda: super)(_n_(463380, "MainWindow", lambda: MainWindow), _n_(463381, "self", lambda: self)), "__init__"))
        _l_(463384)
        _n_(463385, "self", lambda: self).browser = _c_(463387, _n_(463386, "QWebEngineView", lambda: QWebEngineView))
        _l_(463388)
        _c_(463394, _a_(463391, _a_(463390, _n_(463389, "self", lambda: self), "browser"), "setUrl"), _c_(463393, _n_(463392, "QUrl", lambda: QUrl), 'https://www.google.com'))
        _l_(463395)
        _c_(463400, _a_(463397, _n_(463396, "self", lambda: self), "setCentralWidget"), _a_(463399, _n_(463398, "self", lambda: self), "browser"))
        _l_(463401)
        _c_(463404, _a_(463403, _n_(463402, "self", lambda: self), "showMaximized"))
        _l_(463405)
        navbar = _c_(463407, _n_(463406, "QToolBar", lambda: QToolBar))
        _l_(463408)
        _c_(463412, _a_(463410, _n_(463409, "self", lambda: self), "addToolBar"), _n_(463411, "navbar", lambda: navbar))
        _l_(463413)

        back_btn = _c_(463416, _n_(463414, "QAction", lambda: QAction), '<=', _n_(463415, "self", lambda: self))
        _l_(463417)
        _c_(463424, _a_(463420, _a_(463419, _n_(463418, "back_btn", lambda: back_btn), "triggered"), "connect"), _a_(463423, _a_(463422, _n_(463421, "self", lambda: self), "browser"), "back"))
        _l_(463425)
        _c_(463429, _a_(463427, _n_(463426, "navbar", lambda: navbar), "addAction"), _n_(463428, "back_btn", lambda: back_btn))
        _l_(463430)

        forward_btn = _c_(463433, _n_(463431, "QAction", lambda: QAction), '=>', _n_(463432, "self", lambda: self))
        _l_(463434)
        _c_(463441, _a_(463437, _a_(463436, _n_(463435, "forward_btn", lambda: forward_btn), "triggered"), "connect"), _a_(463440, _a_(463439, _n_(463438, "self", lambda: self), "browser"), "forward"))
        _l_(463442)
        _c_(463446, _a_(463444, _n_(463443, "navbar", lambda: navbar), "addAction"), _n_(463445, "forward_btn", lambda: forward_btn))
        _l_(463447)
        reload_btn = _c_(463450, _n_(463448, "QAction", lambda: QAction), 'reload', _n_(463449, "self", lambda: self))
        _l_(463451)
        _c_(463458, _a_(463454, _a_(463453, _n_(463452, "reload_btn", lambda: reload_btn), "triggered"), "connect"), _a_(463457, _a_(463456, _n_(463455, "self", lambda: self), "browser"), "reload"))
        _l_(463459)
        _c_(463463, _a_(463461, _n_(463460, "navbar", lambda: navbar), "addAction"), _n_(463462, "reload_btn", lambda: reload_btn))
        _l_(463464)

        _n_(463465, "self", lambda: self).url_bar = _c_(463468, _n_(463466, "QLineEdit", lambda: QLineEdit), _n_(463467, "self", lambda: self))
        _l_(463469)
        _c_(463474, _a_(463471, _n_(463470, "navbar", lambda: navbar), "addAction"), _a_(463473, _n_(463472, "self", lambda: self), "url_bar"))
        _l_(463475)


APP = _c_(463481, _n_(463478, "QApplication", lambda: QApplication), _a_(463480, _n_(463479, "sys", lambda: sys), "argv"))
_l_(463482)
_c_(463485, _a_(463484, _n_(463483, "QApplication", lambda: QApplication), "setApplicationName"), 'Kahari Go Web')
_l_(463486)
window = _c_(463488, _n_(463487, "MainWindow", lambda: MainWindow))
_l_(463489)
_c_(463492, _a_(463491, _n_(463490, "APP", lambda: APP), "exec_"))
_l_(463493)