# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68688113/python-kivymd-typeerror-init-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(346089)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(346091)

except ImportError:
    pass
try:
    from kivymd.uix.list import *
    _l_(346093)

except ImportError:
    pass

KV = '''
ScrollView:

    MDList:
        id: list
'''
_l_(346094)

class MainApp(_n_(346095, "MDApp", lambda: MDApp)):
    _l_(346119)

    def build(self):
        _l_(346101)

        aux = _c_(346099, _a_(346097, _n_(346096, "Builder", lambda: Builder), "load_string"), _n_(346098, "KV", lambda: KV))
        _l_(346100)
        return aux

    def on_start(self):
        _l_(346118)


        ib = _c_(346103, _n_(346102, "IconLeftWidget", lambda: IconLeftWidget), icon='github')
        _l_(346104)
        ibn = _c_(346108, _n_(346105, "OneLineAvatarIconListItem", lambda: OneLineAvatarIconListItem), _c_(346107, _n_(346106, "IconLeftWidget", lambda: IconLeftWidget), icon='github')
            )
        _l_(346109)
        
        _c_(346116, _a_(346114, _a_(346113, _a_(346112, _a_(346111, _n_(346110, "self", lambda: self), "root"), "ids"), "list"), "add_widget"), _n_(346115, "ib", lambda: ib))
        _l_(346117)

_c_(346123, _a_(346122, _c_(346121, _n_(346120, "MainApp", lambda: MainApp)), "run"))
_l_(346124)