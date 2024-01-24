# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59201728/having-a-problem-with-the-kivy-attribute-error-how-to-fix-attributeerror-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(700370)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(700372)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(700374)

except ImportError:
    pass
try:
    from kivymd.uix.tab import MDTabsBase
    _l_(700376)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(700378)

except ImportError:
    pass
try:
    from kivymd.uix.menu import MDDropdownMenu
    _l_(700380)

except ImportError:
    pass
try:
    from kivy.factory import Factory
    _l_(700382)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(700384)

except ImportError:
    pass
_c_(700387, _a_(700386, _n_(700385, "Builder", lambda: Builder), "load_file"), 'user/user.kv')
_l_(700388)

class MyTab(_n_(700389, "BoxLayout", lambda: BoxLayout), _n_(700390, "MDTabsBase", lambda: MDTabsBase)):
    _l_(700392)

    pass
    _l_(700391)


class MyTab2(_n_(700393, "BoxLayout", lambda: BoxLayout), _n_(700394, "MDTabsBase", lambda: MDTabsBase)):
    _l_(700396)

    pass
    _l_(700395)


class MyTab3(_n_(700397, "BoxLayout", lambda: BoxLayout), _n_(700398, "MDTabsBase", lambda: MDTabsBase)):
    _l_(700400)

    pass
    _l_(700399)


class UserWindow(_n_(700401, "BoxLayout", lambda: BoxLayout)):
    _l_(700408)

    def __init__(self, **kwargs):
        _l_(700407)

        _c_(700405, _a_(700403, _n_(700402, "super", lambda: super)(), "__init__"), **_n_(700404, "kwargs", lambda: kwargs))
        _l_(700406)


class UserApp(_n_(700409, "MDApp", lambda: MDApp)):
    _l_(700490)


    title = 'DEMO'
    _l_(700410)
    dropdown = _c_(700412, _n_(700411, "ObjectProperty", lambda: ObjectProperty))
    _l_(700413)

    def __init__(self, **kwargs):
        _l_(700428)

        _a_(700415, _n_(700414, "self", lambda: self), "theme_cls").theme_style = "Dark"
        _l_(700416)
        _a_(700418, _n_(700417, "self", lambda: self), "theme_cls").primary_palette = "Orange"
        _l_(700419)
        _a_(700421, _n_(700420, "self", lambda: self), "theme_cls").accent_palette = "Gray"
        _l_(700422)
        _c_(700426, _a_(700424, _n_(700423, "super", lambda: super)(), "__init__"), **_n_(700425, "kwargs", lambda: kwargs))
        _l_(700427)

    def on_start(self):
        _l_(700447)

        # Create the dropdown menu
        _n_(700429, "self", lambda: self).dropdown = _c_(700431, _n_(700430, "MDDropdownMenu", lambda: MDDropdownMenu), width_mult=2)
        _l_(700432)

        # Add items to the menu
        for i in _c_(700434, _n_(700433, "range", lambda: range), 6):
            _l_(700446)

            _c_(700444, _a_(700438, _a_(700437, _a_(700436, _n_(700435, "self", lambda: self), "dropdown"), "items"), "append"), {"viewclass": "MDMenuItem",
                 "text": "Option " + _c_(700441, _n_(700439, "str", lambda: str), _n_(700440, "i", lambda: i)),
                 "callback": _a_(700443, _n_(700442, "self", lambda: self), "option_callback")}
            )
            _l_(700445)

    def option_callback(self, text_of_the_option):
        _l_(700452)

        _c_(700450, _n_(700448, "print", lambda: print), _n_(700449, "text_of_the_option", lambda: text_of_the_option))
        _l_(700451)

    def build(self):
        _l_(700489)

        screen = _c_(700455, _a_(700454, _n_(700453, "Factory", lambda: Factory), "UserWindow"))
        _l_(700456)

        tab = _c_(700458, _n_(700457, "MyTab", lambda: MyTab), text='Home Tab')
        _l_(700459)
        _c_(700465, _a_(700463, _a_(700462, _a_(700461, _n_(700460, "screen", lambda: screen), "ids"), "android_tabs"), "add_widget"), _n_(700464, "tab", lambda: tab))
        _l_(700466)

        tab = _c_(700468, _n_(700467, "MyTab2", lambda: MyTab2), text='Approved Tickets')
        _l_(700469)
        _c_(700475, _a_(700473, _a_(700472, _a_(700471, _n_(700470, "screen", lambda: screen), "ids"), "android_tabs"), "add_widget"), _n_(700474, "tab", lambda: tab))
        _l_(700476)

        tab = _c_(700478, _n_(700477, "MyTab3", lambda: MyTab3), text='History')
        _l_(700479)
        _c_(700485, _a_(700483, _a_(700482, _a_(700481, _n_(700480, "screen", lambda: screen), "ids"), "android_tabs"), "add_widget"), _n_(700484, "tab", lambda: tab))
        _l_(700486)
        aux = _n_(700487, "screen", lambda: screen)
        _l_(700488)
        return aux


if _n_(700491, "__name__", lambda: __name__) == '__main__':
    _l_(700499)

    oa = _c_(700493, _n_(700492, "UserApp", lambda: UserApp))
    _l_(700494)
    _c_(700497, _a_(700496, _n_(700495, "oa", lambda: oa), "run"))
    _l_(700498)