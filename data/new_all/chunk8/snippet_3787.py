# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68046076/sm-current-does-not-switch-screen-and-gives-me-attribute-error-str-object-ha
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(590504)

except ImportError:
    pass
try:
    from kivy.lang.builder import Builder
    _l_(590506)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen, ScreenManager
    _l_(590508)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(590510)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(590512)

except ImportError:
    pass

_n_(590513, "Window", lambda: Window).size = (350, 580)
_l_(590514)


class Welcome(_n_(590515, "Screen", lambda: Screen)):
    _l_(590538)

    emailInput = _c_(590517, _n_(590516, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(590518)
    passwordInput = _c_(590520, _n_(590519, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(590521)

    def validatelogin(self):
        _l_(590537)

        if _a_(590524, _a_(590523, _n_(590522, "self", lambda: self), "emailInput"), "text") == "123" and _a_(590527, _a_(590526, _n_(590525, "self", lambda: self), "passwordInput"), "text") == "123":
            _l_(590536)

            _c_(590531, _n_(590528, "print", lambda: print), "????", _a_(590530, _n_(590529, "self", lambda: self), "manager"))
            _l_(590532)
            _a_(590534, _n_(590533, "self", lambda: self), "manager").current = 'selection'
            _l_(590535)


class SelectionOption(_n_(590539, "Screen", lambda: Screen)):
    _l_(590541)

    pass
    _l_(590540)


class windowManager(_n_(590542, "ScreenManager", lambda: ScreenManager)):
    _l_(590544)

    pass
    _l_(590543)


class Console(_n_(590545, "MDApp", lambda: MDApp)):
    _l_(590551)


    def build(self):
        _l_(590550)

        aux = _c_(590548, _a_(590547, _n_(590546, "Builder", lambda: Builder), "load_file"), '../Files/ScreenManager.kv')
        _l_(590549)
        return aux


if _n_(590552, "__name__", lambda: __name__) == '__main__':
    _l_(590558)

    _c_(590556, _a_(590555, _c_(590554, _n_(590553, "Console", lambda: Console)), "run"))
    _l_(590557)