# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63958900/attributeerror-snackbar-object-has-no-attribute-show
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(385590)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(385592)

except ImportError:
    pass
try:
    from kivymd.uix.snackbar import Snackbar
    _l_(385594)

except ImportError:
    pass

KV = '''
BoxLayout:
    MDRaisedButton:
        text: "click"
        on_press: app.test_bar()
'''
_l_(385595)

class TestApp(_n_(385596, "MDApp", lambda: MDApp)):
    _l_(385609)

    def build(self):
        _l_(385602)

        aux = _c_(385600, _a_(385598, _n_(385597, "Builder", lambda: Builder), "load_string"), _n_(385599, "KV", lambda: KV))
        _l_(385601)
        return aux
    
    def test_bar(self):
        _l_(385608)

        _c_(385606, _a_(385605, _c_(385604, _n_(385603, "Snackbar", lambda: Snackbar), text="Hello world!"), "show"))
        _l_(385607)

_c_(385613, _a_(385612, _c_(385611, _n_(385610, "TestApp", lambda: TestApp)), "run"))
_l_(385614)