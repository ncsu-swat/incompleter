# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77323400/error-kivy-attributeerror-final-object-has-no-attribute-ganar-juego
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.uix.popup import Popup
    _l_(618755)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(618757)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(618759)

except ImportError:
    pass


class Final(_n_(618760, "Popup", lambda: Popup)):
    _l_(618783)


    def __init__(self, **kwargs):
        _l_(618773)

        _c_(618763, _a_(618762, _n_(618761, "super", lambda: super)(), "__init__"))
        _l_(618764)
        _n_(618765, "self", lambda: self).ganar_juego = _n_(618766, "kwargs", lambda: kwargs)["ganador"]
        _l_(618767)
        _c_(618771, _n_(618768, "print", lambda: print), _a_(618770, _n_(618769, "self", lambda: self), "ganar_juego"))
        _l_(618772)
    def on_kv_post(self, base_widget):
        _l_(618782)

        #Selecciono si ha ganado o no
        _a_(618776, _a_(618775, _n_(618774, "self", lambda: self), "ids"), "ganar").text = _c_(618780, _n_(618777, "str", lambda: str), _a_(618779, _n_(618778, "self", lambda: self), "ganar_juego"))
        _l_(618781)