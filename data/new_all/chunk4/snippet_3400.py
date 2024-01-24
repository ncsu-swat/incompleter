# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74895052/python-attributeerror-module-core-has-no-attribute-children
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(640954)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager
    _l_(640956)

except ImportError:
    pass

_c_(640959, _a_(640958, _n_(640957, "Builder", lambda: Builder), "load_file"), "layouts/screen_manager.kv")
_l_(640960)


class WindowManager(_n_(640961, "ScreenManager", lambda: ScreenManager)):
    _l_(640963)

    pass
    _l_(640962)