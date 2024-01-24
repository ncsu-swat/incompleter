# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59201728/having-a-problem-with-the-kivy-attribute-error-how-to-fix-attributeerror-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(703854)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(703856)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(703858)

except ImportError:
    pass
try:
    from kivymd.uix.tab import MDTabsBase
    _l_(703860)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(703862)

except ImportError:
    pass
try:
    from kivymd.uix.menu import MDDropdownMenu
    _l_(703864)

except ImportError:
    pass
try:
    from kivy.factory import Factory
    _l_(703866)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(703868)

except ImportError:
    pass
_c_(703871, _a_(703870, _n_(703869, "Builder", lambda: Builder), "load_file"), 'user/user.kv')
_l_(703872)

class MyTab(_n_(703873, "BoxLayout", lambda: BoxLayout), _n_(703874, "MDTabsBase", lambda: MDTabsBase)):
    _l_(703876)

    pass
    _l_(703875)


class MyTab2(_n_(703877, "BoxLayout", lambda: BoxLayout), _n_(703878, "MDTabsBase", lambda: MDTabsBase)):
    _l_(703880)

    pass
    _l_(703879)


class MyTab3(_n_(703881, "BoxLayout", lambda: BoxLayout), _n_(703882, "MDTabsBase", lambda: MDTabsBase)):
    _l_(703884)

    pass
    _l_(703883)


class UserWindow(_n_(703885, "BoxLayout", lambda: BoxLayout)):
    _l_(703892)

    def __init__(self, **kwargs):
        _l_(703891)

        _c_(703889, _a_(703887, _n_(703886, "super", lambda: super)(), "__init__"), **_n_(703888, "kwargs", lambda: kwargs))
        _l_(703890)


class UserApp(_n_(703893, "MDApp", lambda: MDApp)):
    _l_(703974)


    title = 'DEMO'
    _l_(703894)
    dropdown = _c_(703896, _n_(703895, "ObjectProperty", lambda: ObjectProperty))
    _l_(703897)

    def __init__(self, **kwargs):
        _l_(703912)

        _a_(703899, _n_(703898, "self", lambda: self), "theme_cls").theme_style = "Dark"
        _l_(703900)
        _a_(703902, _n_(703901, "self", lambda: self), "theme_cls").primary_palette = "Orange"
        _l_(703903)
        _a_(703905, _n_(703904, "self", lambda: self), "theme_cls").accent_palette = "Gray"
        _l_(703906)
        _c_(703910, _a_(703908, _n_(703907, "super", lambda: super)(), "__init__"), **_n_(703909, "kwargs", lambda: kwargs))
        _l_(703911)

    def on_start(self):
        _l_(703931)

        # Create the dropdown menu
        _n_(703913, "self", lambda: self).dropdown = _c_(703915, _n_(703914, "MDDropdownMenu", lambda: MDDropdownMenu), width_mult=2)
        _l_(703916)

        # Add items to the menu
        for i in _c_(703918, _n_(703917, "range", lambda: range), 6):
            _l_(703930)

            _c_(703928, _a_(703922, _a_(703921, _a_(703920, _n_(703919, "self", lambda: self), "dropdown"), "items"), "append"), {"viewclass": "MDMenuItem",
                 "text": "Option " + _c_(703925, _n_(703923, "str", lambda: str), _n_(703924, "i", lambda: i)),
                 "callback": _a_(703927, _n_(703926, "self", lambda: self), "option_callback")}
            )
            _l_(703929)

    def option_callback(self, text_of_the_option):
        _l_(703936)

        _c_(703934, _n_(703932, "print", lambda: print), _n_(703933, "text_of_the_option", lambda: text_of_the_option))
        _l_(703935)

    def build(self):
        _l_(703973)

        screen = _c_(703939, _a_(703938, _n_(703937, "Factory", lambda: Factory), "UserWindow"))
        _l_(703940)

        tab = _c_(703942, _n_(703941, "MyTab", lambda: MyTab), text='Home Tab')
        _l_(703943)
        _c_(703949, _a_(703947, _a_(703946, _a_(703945, _n_(703944, "screen", lambda: screen), "ids"), "android_tabs"), "add_widget"), _n_(703948, "tab", lambda: tab))
        _l_(703950)

        tab = _c_(703952, _n_(703951, "MyTab2", lambda: MyTab2), text='Approved Tickets')
        _l_(703953)
        _c_(703959, _a_(703957, _a_(703956, _a_(703955, _n_(703954, "screen", lambda: screen), "ids"), "android_tabs"), "add_widget"), _n_(703958, "tab", lambda: tab))
        _l_(703960)

        tab = _c_(703962, _n_(703961, "MyTab3", lambda: MyTab3), text='History')
        _l_(703963)
        _c_(703969, _a_(703967, _a_(703966, _a_(703965, _n_(703964, "screen", lambda: screen), "ids"), "android_tabs"), "add_widget"), _n_(703968, "tab", lambda: tab))
        _l_(703970)
        aux = _n_(703971, "screen", lambda: screen)
        _l_(703972)
        return aux


if _n_(703975, "__name__", lambda: __name__) == '__main__':
    _l_(703983)

    oa = _c_(703977, _n_(703976, "UserApp", lambda: UserApp))
    _l_(703978)
    _c_(703981, _a_(703980, _n_(703979, "oa", lambda: oa), "run"))
    _l_(703982)