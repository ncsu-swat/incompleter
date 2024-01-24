# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74895052/python-attributeerror-module-core-has-no-attribute-children
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(635459)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen
    _l_(635461)

except ImportError:
    pass
try:
    from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
    _l_(635463)

except ImportError:
    pass
try:
    from application.database.vaccination_calendar import get_children
    _l_(635465)

except ImportError:
    pass

_c_(635468, _a_(635467, _n_(635466, "Builder", lambda: Builder), "load_file"), "layouts/children.kv")
_l_(635469)

class Children(_n_(635470, "Screen", lambda: Screen)):
    _l_(635472)

    pass
    _l_(635471)