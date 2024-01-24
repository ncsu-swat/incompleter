# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60126786/nameerror-instance-of-windowmanager-is-not-defined-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(657134)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(657136)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
    _l_(657138)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(657140)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(657142)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(657144)

except ImportError:
    pass
try:
    from kivy.core.text import Label as CoreLabel
    _l_(657146)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(657148)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(657150)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(657152)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(657154)

except ImportError:
    pass
try:
    from kivymd.uix.picker import MDDatePicker
    _l_(657156)

except ImportError:
    pass
try:
    from kivymd.uix.textfield import MDTextField
    _l_(657158)

except ImportError:
    pass
try:
    from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatIconButton
    _l_(657160)

except ImportError:
    pass
try:
    from kivymd.uix.dialog import MDDialog
    _l_(657162)

except ImportError:
    pass
try:
    from kivy.uix.scrollview import ScrollView
    _l_(657164)

except ImportError:
    pass
try:
    from kivy.uix.dropdown import DropDown
    _l_(657166)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(657168)

except ImportError:
    pass
try:
    from kivy.uix.relativelayout import RelativeLayout
    _l_(657170)

except ImportError:
    pass


_n_(657171, "Window", lambda: Window).clearcolor = (1,1,1,1)
_l_(657172)

mydb = _c_(657175, _a_(657174, _a_(657173, mysql, "connector"), "connect"), host="localhost",
  user="root",
  passwd="",
  database=""
         )
_l_(657176)

cur = _c_(657179, _a_(657178, _n_(657177, "mydb", lambda: mydb), "cursor"))
_l_(657180)

_c_(657183, _a_(657182, _n_(657181, "cur", lambda: cur), "execute"), "CREATE DATABASE IF NOT EXISTS meet")
_l_(657184)

_c_(657187, _a_(657186, _n_(657185, "cur", lambda: cur), "execute"), "CREATE TABLE IF NOT EXISTS users (email VARCHAR(255), password VARCHAR(255))")
_l_(657188)

_c_(657191, _a_(657190, _n_(657189, "cur", lambda: cur), "close"))
_l_(657192)
_c_(657195, _a_(657194, _n_(657193, "mydb", lambda: mydb), "close"))
_l_(657196)


class LoginWindow(_n_(657197, "Screen", lambda: Screen)):
    _l_(657252)

    password = _c_(657199, _n_(657198, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657200)

    def login(self, email):
        _l_(657244)

        mydb = _c_(657203, _a_(657202, _a_(657201, mysql, "connector"), "connect"), host="localhost", user="root", passwd="", database="")
        _l_(657204)
        cur = _c_(657207, _a_(657206, _n_(657205, "mydb", lambda: mydb), "cursor"), buffered=True)
        _l_(657208)
        _c_(657215, _a_(657210, _n_(657209, "cur", lambda: cur), "execute"), "SELECT * FROM users WHERE email = %s and password = %s", (_n_(657211, "email", lambda: email), _a_(657214, _a_(657213, _n_(657212, "self", lambda: self), "password"), "text")))
        _l_(657216)
        result = _c_(657219, _a_(657218, _n_(657217, "cur", lambda: cur), "fetchone"))
        _l_(657220)
        _c_(657223, _a_(657222, _n_(657221, "mydb", lambda: mydb), "commit"))
        _l_(657224)
        _c_(657227, _a_(657226, _n_(657225, "cur", lambda: cur), "close"))
        _l_(657228)
        _c_(657231, _a_(657230, _n_(657229, "mydb", lambda: mydb), "close"))
        _l_(657232)
        if _n_(657233, "result", lambda: result):
            _l_(657243)

            _c_(657236, _a_(657235, _n_(657234, "self", lambda: self), "reset"))
            _l_(657237)
            _n_(657238, "sm", lambda: sm).current = "information"
            _l_(657239)
        else:
            _c_(657241, _n_(657240, "invalid_login", lambda: invalid_login))
            _l_(657242)

    def reset(self):
        _l_(657251)

        _a_(657246, _n_(657245, "self", lambda: self), "email").text = ""
        _l_(657247)
        _a_(657249, _n_(657248, "self", lambda: self), "password").text = ""
        _l_(657250)


class WindowManager(_n_(657253, "ScreenManager", lambda: ScreenManager)):
    _l_(657255)

    pass
    _l_(657254)


class MyApp(_n_(657256, "App", lambda: App)):
    _l_(657284)

    theme_cls = _c_(657258, _n_(657257, "ThemeManager", lambda: ThemeManager))
    _l_(657259)

    def build(self):
        _l_(657283)

        kv = _c_(657262, _a_(657261, _n_(657260, "Builder", lambda: Builder), "load_file"), "kivy.kv")
        _l_(657263)
        sm = _c_(657265, _n_(657264, "WindowManager", lambda: WindowManager))
        _l_(657266)

        screens = [_c_(657268, _n_(657267, "LoginWindow", lambda: LoginWindow), name="login"),
                   _c_(657270, _n_(657269, "Information", lambda: Information), name="information")]
        _l_(657271)
        for screen in _n_(657272, "screens", lambda: screens):
            _l_(657278)

            _c_(657276, _a_(657274, _n_(657273, "sm", lambda: sm), "add_widget"), _n_(657275, "screen", lambda: screen))
            _l_(657277)

        _n_(657279, "sm", lambda: sm).current = "login"
        _l_(657280)
        aux = _n_(657281, "sm", lambda: sm)
        _l_(657282)
        return aux


if _n_(657285, "__name__", lambda: __name__) == '__main__':
    _l_(657291)

    _c_(657289, _a_(657288, _c_(657287, _n_(657286, "MyApp", lambda: MyApp)), "run"))
    _l_(657290)