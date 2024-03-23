# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76718942/attributeerror-super-object-has-no-attribute-getattr-did-you-mean
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(589051)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager
    _l_(589053)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen
    _l_(589055)

except ImportError:
    pass
try:
    from kivymd.uix.screen import MDScreen
    _l_(589057)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(589059)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(589061)

except ImportError:
    pass
_n_(589062, "Window", lambda: Window).size = (360,640)
_l_(589063)

class Main(_n_(589064, "MDApp", lambda: MDApp)):
    _l_(589113)

    def build(self):
        _l_(589091)

        screenmanager = _c_(589066, _n_(589065, "ScreenManager", lambda: ScreenManager))
        _l_(589067)
        _c_(589073, _a_(589069, _n_(589068, "screenmanager", lambda: screenmanager), "add_widget"), _c_(589072, _a_(589071, _n_(589070, "Builder", lambda: Builder), "load_file"), "kv/key.kv"))
        _l_(589074)
        _c_(589080, _a_(589076, _n_(589075, "screenmanager", lambda: screenmanager), "add_widget"), _c_(589079, _a_(589078, _n_(589077, "Builder", lambda: Builder), "load_file"), "kv/home.kv"))
        _l_(589081)
        _c_(589087, _a_(589083, _n_(589082, "screenmanager", lambda: screenmanager), "add_widget"), _c_(589086, _a_(589085, _n_(589084, "Builder", lambda: Builder), "load_file"), "kv/menu.kv"))
        _l_(589088)
        aux = _n_(589089, "screenmanager", lambda: screenmanager)
        _l_(589090)
        return aux
    def keylogin(self, kode_key, nohp):
        _l_(589093)

        pass
        _l_(589092)
    def kodee(self):
        _l_(589112)

        kode_key = _a_(589098, _a_(589097, _a_(589096, _a_(589095, _n_(589094, "self", lambda: self), "root"), "ids"), "key_login"), "text")
        _l_(589099)
        nohp = _a_(589104, _a_(589103, _a_(589102, _a_(589101, _n_(589100, "self", lambda: self), "root"), "ids"), "nomor_hp"), "text")
        _l_(589105)
        _c_(589110, _a_(589107, _n_(589106, "self", lambda: self), "keylogin"), _n_(589108, "kode_key", lambda: kode_key), _n_(589109, "nohp", lambda: nohp))
        _l_(589111)



if _n_(589114, "__name__", lambda: __name__) == "__main__":
    _l_(589120)

    _c_(589118, _a_(589117, _c_(589116, _n_(589115, "Main", lambda: Main)), "run"))
    _l_(589119)