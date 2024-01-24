# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59461791/kivymd-attributeerror-nonetype-object-has-no-attribute-theme-cls
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(448563)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(448565)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
    _l_(448567)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(448569)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(448571)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(448573)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(448575)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(448577)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(448579)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(448581)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(448583)

except ImportError:
    pass


_n_(448584, "Window", lambda: Window).clearcolor = (1,1,1,1)
_l_(448585)


class Information(_n_(448586, "Screen", lambda: Screen)):
    _l_(448588)

    pass
    _l_(448587)


class WindowManager(_n_(448589, "ScreenManager", lambda: ScreenManager)):
    _l_(448591)

    pass
    _l_(448590)


kv = _c_(448594, _a_(448593, _n_(448592, "Builder", lambda: Builder), "load_file"), "kivy.kv")
_l_(448595)
sm = _c_(448597, _n_(448596, "WindowManager", lambda: WindowManager))
_l_(448598)

screens = [_c_(448600, _n_(448599, "Information", lambda: Information), name="information")]
_l_(448601)
for screen in _n_(448602, "screens", lambda: screens):
    _l_(448608)

    _c_(448606, _a_(448604, _n_(448603, "sm", lambda: sm), "add_widget"), _n_(448605, "screen", lambda: screen))
    _l_(448607)

_n_(448609, "sm", lambda: sm).current = "information"
_l_(448610)


class MyApp(_n_(448611, "App", lambda: App)):
    _l_(448618)

    theme_cls = _c_(448613, _n_(448612, "ThemeManager", lambda: ThemeManager))
    _l_(448614)

    def build(self):
        _l_(448617)

        aux = _n_(448615, "sm", lambda: sm)
        _l_(448616)
        return aux


if _n_(448619, "__name__", lambda: __name__) == '__main__':
    _l_(448625)

    _c_(448623, _a_(448622, _c_(448621, _n_(448620, "MyApp", lambda: MyApp)), "run"))
    _l_(448624)