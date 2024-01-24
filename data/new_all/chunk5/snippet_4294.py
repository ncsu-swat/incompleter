# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60126786/nameerror-instance-of-windowmanager-is-not-defined-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(651751)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(651753)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
    _l_(651755)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(651757)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(651759)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(651761)

except ImportError:
    pass
try:
    from kivy.core.text import Label as CoreLabel
    _l_(651763)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(651765)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(651767)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(651769)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(651771)

except ImportError:
    pass
try:
    from kivymd.uix.picker import MDDatePicker
    _l_(651773)

except ImportError:
    pass
try:
    from kivymd.uix.textfield import MDTextField
    _l_(651775)

except ImportError:
    pass
try:
    from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatIconButton
    _l_(651777)

except ImportError:
    pass
try:
    from kivymd.uix.dialog import MDDialog
    _l_(651779)

except ImportError:
    pass
try:
    from kivy.uix.scrollview import ScrollView
    _l_(651781)

except ImportError:
    pass
try:
    from kivy.uix.dropdown import DropDown
    _l_(651783)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(651785)

except ImportError:
    pass
try:
    from kivy.uix.relativelayout import RelativeLayout
    _l_(651787)

except ImportError:
    pass


_n_(651788, "Window", lambda: Window).clearcolor = (1,1,1,1)
_l_(651789)

mydb = _c_(651792, _a_(651791, _a_(651790, mysql, "connector"), "connect"), host="localhost",
  user="root",
  passwd="",
  database=""
         )
_l_(651793)

cur = _c_(651796, _a_(651795, _n_(651794, "mydb", lambda: mydb), "cursor"))
_l_(651797)

_c_(651800, _a_(651799, _n_(651798, "cur", lambda: cur), "execute"), "CREATE DATABASE IF NOT EXISTS meet")
_l_(651801)

_c_(651804, _a_(651803, _n_(651802, "cur", lambda: cur), "execute"), "CREATE TABLE IF NOT EXISTS users (email VARCHAR(255), password VARCHAR(255))")
_l_(651805)

_c_(651808, _a_(651807, _n_(651806, "cur", lambda: cur), "close"))
_l_(651809)
_c_(651812, _a_(651811, _n_(651810, "mydb", lambda: mydb), "close"))
_l_(651813)


class LoginWindow(_n_(651814, "Screen", lambda: Screen)):
    _l_(651869)

    password = _c_(651816, _n_(651815, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(651817)

    def login(self, email):
        _l_(651861)

        mydb = _c_(651820, _a_(651819, _a_(651818, mysql, "connector"), "connect"), host="localhost", user="root", passwd="", database="")
        _l_(651821)
        cur = _c_(651824, _a_(651823, _n_(651822, "mydb", lambda: mydb), "cursor"), buffered=True)
        _l_(651825)
        _c_(651832, _a_(651827, _n_(651826, "cur", lambda: cur), "execute"), "SELECT * FROM users WHERE email = %s and password = %s", (_n_(651828, "email", lambda: email), _a_(651831, _a_(651830, _n_(651829, "self", lambda: self), "password"), "text")))
        _l_(651833)
        result = _c_(651836, _a_(651835, _n_(651834, "cur", lambda: cur), "fetchone"))
        _l_(651837)
        _c_(651840, _a_(651839, _n_(651838, "mydb", lambda: mydb), "commit"))
        _l_(651841)
        _c_(651844, _a_(651843, _n_(651842, "cur", lambda: cur), "close"))
        _l_(651845)
        _c_(651848, _a_(651847, _n_(651846, "mydb", lambda: mydb), "close"))
        _l_(651849)
        if _n_(651850, "result", lambda: result):
            _l_(651860)

            _c_(651853, _a_(651852, _n_(651851, "self", lambda: self), "reset"))
            _l_(651854)
            _n_(651855, "sm", lambda: sm).current = "information"
            _l_(651856)
        else:
            _c_(651858, _n_(651857, "invalid_login", lambda: invalid_login))
            _l_(651859)

    def reset(self):
        _l_(651868)

        _a_(651863, _n_(651862, "self", lambda: self), "email").text = ""
        _l_(651864)
        _a_(651866, _n_(651865, "self", lambda: self), "password").text = ""
        _l_(651867)


class WindowManager(_n_(651870, "ScreenManager", lambda: ScreenManager)):
    _l_(651872)

    pass
    _l_(651871)


class MyApp(_n_(651873, "App", lambda: App)):
    _l_(651901)

    theme_cls = _c_(651875, _n_(651874, "ThemeManager", lambda: ThemeManager))
    _l_(651876)

    def build(self):
        _l_(651900)

        kv = _c_(651879, _a_(651878, _n_(651877, "Builder", lambda: Builder), "load_file"), "kivy.kv")
        _l_(651880)
        sm = _c_(651882, _n_(651881, "WindowManager", lambda: WindowManager))
        _l_(651883)

        screens = [_c_(651885, _n_(651884, "LoginWindow", lambda: LoginWindow), name="login"),
                   _c_(651887, _n_(651886, "Information", lambda: Information), name="information")]
        _l_(651888)
        for screen in _n_(651889, "screens", lambda: screens):
            _l_(651895)

            _c_(651893, _a_(651891, _n_(651890, "sm", lambda: sm), "add_widget"), _n_(651892, "screen", lambda: screen))
            _l_(651894)

        _n_(651896, "sm", lambda: sm).current = "login"
        _l_(651897)
        aux = _n_(651898, "sm", lambda: sm)
        _l_(651899)
        return aux


if _n_(651902, "__name__", lambda: __name__) == '__main__':
    _l_(651908)

    _c_(651906, _a_(651905, _c_(651904, _n_(651903, "MyApp", lambda: MyApp)), "run"))
    _l_(651907)