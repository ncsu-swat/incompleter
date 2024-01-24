# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69085989/error-attributeerror-kivy-properties-objectproperty-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(590878)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(590880)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(590882)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty, StringProperty
    _l_(590884)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(590886)

except ImportError:
    pass
_n_(590887, "Window", lambda: Window).size = (1280, 720)
_l_(590888)


class LoginScreen(_n_(590889, "Screen", lambda: Screen)):
    _l_(590922)

    username = _c_(590891, _n_(590890, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(590892)
    password = _c_(590894, _n_(590893, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(590895)

    def show_data(self, obj):
        _l_(590921)

        _c_(590907, _a_(590897, _n_(590896, "client", lambda: client), "send"), _c_(590906, _a_(590899, _n_(590898, "pickle", lambda: pickle), "dumps"), ['login', _a_(590902, _a_(590901, _n_(590900, "self", lambda: self), "username"), "text"), _a_(590905, _a_(590904, _n_(590903, "self", lambda: self), "password"), "text")]))
        _l_(590908)
        _n_(590909, "MenuScreen", lambda: MenuScreen).data = _c_(590915, _a_(590911, _n_(590910, "pickle", lambda: pickle), "loads"), _c_(590914, _a_(590913, _n_(590912, "client", lambda: client), "recv"), 1024))
        _l_(590916)
        _c_(590919, _a_(590918, _n_(590917, "MenuScreen", lambda: MenuScreen), "get_data"))
        _l_(590920)

class MenuScreen(_n_(590923, "Screen", lambda: Screen)):
    _l_(590943)

    data = '_'
    _l_(590924)
    menuName = _c_(590926, _n_(590925, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(590927)
    menuBalance = _c_(590929, _n_(590928, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(590930)

    @_n_(590931, "classmethod", lambda: classmethod)
    def get_data(self):
        _l_(590942)

        _a_(590933, _n_(590932, "self", lambda: self), "menuName").text = _a_(590935, _n_(590934, "self", lambda: self), "data")[0][0]
        _l_(590936)
        _a_(590938, _n_(590937, "self", lambda: self), "menuBalance").text = _a_(590940, _n_(590939, "self", lambda: self), "data")[0][1]
        _l_(590941)


sm = _c_(590945, _n_(590944, "ScreenManager", lambda: ScreenManager))
_l_(590946)
_c_(590951, _a_(590948, _n_(590947, "sm", lambda: sm), "add_widget"), _c_(590950, _n_(590949, "LoginScreen", lambda: LoginScreen), name='login'))
_l_(590952)
_c_(590957, _a_(590954, _n_(590953, "sm", lambda: sm), "add_widget"), _c_(590956, _n_(590955, "MenuScreen", lambda: MenuScreen), name='menu'))
_l_(590958)

class DemoApp(_n_(590959, "MDApp", lambda: MDApp)):
    _l_(590974)

    def build(self):
        _l_(590973)

        _a_(590961, _n_(590960, "self", lambda: self), "theme_cls").primary_palette = 'Pink'
        _l_(590962)
        _a_(590964, _n_(590963, "self", lambda: self), "theme_cls").theme_style = 'Light'
        _l_(590965)
        screen = _c_(590969, _a_(590967, _n_(590966, "Builder", lambda: Builder), "load_string"), _n_(590968, "screen_helper", lambda: screen_helper))
        _l_(590970)
        aux = _n_(590971, "screen", lambda: screen)
        _l_(590972)
        # Clock.schedule_interval(MenuScreen.name_ret, 15)
        return aux


_c_(590978, _a_(590977, _c_(590976, _n_(590975, "DemoApp", lambda: DemoApp)), "run"))
_l_(590979)