# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56824210/typeerror-nonetype-object-is-not-subscriptable-kivy-package-problem
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(674129)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(674131)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(674133)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(674135)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(674137)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(674139)

except ImportError:
    pass
try:
    import sqlite3
    _l_(674141)

except ImportError:
    pass

conn = _c_(674144, _a_(674143, _n_(674142, "sqlite3", lambda: sqlite3), "connect"), ":memory:")
_l_(674145)
cur = _c_(674148, _a_(674147, _n_(674146, "conn", lambda: conn), "cursor"))
_l_(674149)

_c_(674152, _a_(674151, _n_(674150, "cur", lambda: cur), "execute"), """CREATE TABLE votes (email NOT NULL, password NOT NULL, votes_yes INTEGER, votes_no INTEGER)""")
_l_(674153)


class LoginWindow(_n_(674154, "Screen", lambda: Screen)):
    _l_(674190)

    email = _c_(674156, _n_(674155, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(674157)
    password = _c_(674159, _n_(674158, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(674160)

    def login(self):
        _l_(674182)

        with _n_(674161, "conn", lambda: conn):
            _l_(674181)

            _c_(674164, _a_(674163, _n_(674162, "cur", lambda: cur), "execute"), "SELECT * FROM votes WHERE email = ? And password = ?, (self.email.text, self.password.text)")
            _l_(674165)
            result = _c_(674168, _a_(674167, _n_(674166, "cur", lambda: cur), "fetchone"))
            _l_(674169)
            if _n_(674170, "result", lambda: result):
                _l_(674180)

                _c_(674173, _a_(674172, _n_(674171, "self", lambda: self), "reset"))
                _l_(674174)
                _n_(674175, "sm", lambda: sm).current = "voting"
                _l_(674176)
            else:
                _c_(674178, _n_(674177, "invalid_login", lambda: invalid_login))
                _l_(674179)

    def reset(self):
        _l_(674189)

        _a_(674184, _n_(674183, "self", lambda: self), "email").text = ""
        _l_(674185)
        _a_(674187, _n_(674186, "self", lambda: self), "password").text = ""
        _l_(674188)


class VotingWindow(_n_(674191, "Screen", lambda: Screen)):
    _l_(674209)

    email = _c_(674193, _n_(674192, "ObjectProperty", lambda: ObjectProperty))
    _l_(674194)

    def yes_btn(self):
        _l_(674201)

        with _n_(674195, "conn", lambda: conn):
            _l_(674200)

            _c_(674198, _a_(674197, _n_(674196, "cur", lambda: cur), "execute"), "UPDATE votes set vote_yes = 1 WHERE email = self.email.text")
            _l_(674199)

    def no_btn(self):
        _l_(674208)

        with _n_(674202, "conn", lambda: conn):
            _l_(674207)

            _c_(674205, _a_(674204, _n_(674203, "cur", lambda: cur), "execute"), "UPDATE votes set vote_no = 1 WHERE email = self.email.text")
            _l_(674206)


class CreateAccountWindow(_n_(674210, "Screen", lambda: Screen)):
    _l_(674244)

    email = _c_(674212, _n_(674211, "ObjectProperty", lambda: ObjectProperty))
    _l_(674213)
    password = _c_(674215, _n_(674214, "ObjectProperty", lambda: ObjectProperty))
    _l_(674216)

    def create_btn(self):
        _l_(674236)

        with _n_(674217, "conn", lambda: conn):
            _l_(674235)

            results = _c_(674220, _a_(674219, _n_(674218, "cur", lambda: cur), "execute"), "SELECT * FROM votes WHERE email = ?, (self.email.text,)")
            _l_(674221)
            if _n_(674222, "results", lambda: results):
                _l_(674234)

                _c_(674224, _n_(674223, "invalid_form", lambda: invalid_form))
                _l_(674225)
            else:
                _c_(674228, _a_(674227, _n_(674226, "cur", lambda: cur), "execute"), "INSERT into votes VALUES(email = ?, password = ?), (self.email.text, self.password.text)")
                _l_(674229)
                _c_(674232, _a_(674231, _n_(674230, "self", lambda: self), "reset"))
                _l_(674233)

    def reset(self):
        _l_(674243)

        _a_(674238, _n_(674237, "self", lambda: self), "email").text = ""
        _l_(674239)
        _a_(674241, _n_(674240, "self", lambda: self), "password").text = ""
        _l_(674242)


class WindowManager(_n_(674245, "ScreenManager", lambda: ScreenManager)):
    _l_(674247)

    pass
    _l_(674246)


def invalid_login():
    _l_(674257)

    pop = _c_(674251, _n_(674248, "Popup", lambda: Popup), title='Invalid Login',
                  content=_c_(674250, _n_(674249, "Label", lambda: Label), text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    _l_(674252)
    _c_(674255, _a_(674254, _n_(674253, "pop", lambda: pop), "open"))
    _l_(674256)

def invalid_form():
    _l_(674267)

    pop = _c_(674261, _n_(674258, "Popup", lambda: Popup), title='Error',
                  content=_c_(674260, _n_(674259, "Label", lambda: Label), text='An account already exists with that email address'),
                  size_hint=(None, None), size=(400, 400))
    _l_(674262)
    _c_(674265, _a_(674264, _n_(674263, "pop", lambda: pop), "open"))
    _l_(674266)


kv = _c_(674270, _a_(674269, _n_(674268, "Builder", lambda: Builder), "load_file"), "my.kv")
_l_(674271)
sm = _c_(674273, _n_(674272, "WindowManager", lambda: WindowManager))
_l_(674274)

screens = [_c_(674276, _n_(674275, "LoginWindow", lambda: LoginWindow), name="login"), _c_(674278, _n_(674277, "CreateAccountWindow", lambda: CreateAccountWindow), name="create account"), _c_(674280, _n_(674279, "VotingWindow", lambda: VotingWindow), name="voting")]
_l_(674281)
for screen in _n_(674282, "screens", lambda: screens):
    _l_(674288)

    _c_(674286, _a_(674284, _n_(674283, "sm", lambda: sm), "add_widget"), _n_(674285, "screen", lambda: screen))
    _l_(674287)

_n_(674289, "sm", lambda: sm).current = "login"
_l_(674290)


class MyApp(_n_(674291, "App", lambda: App)):
    _l_(674295)

    def build(self):
        _l_(674294)

        aux = _n_(674292, "sm", lambda: sm)
        _l_(674293)
        return aux


if _n_(674296, "__name__", lambda: __name__) == '__main__':
    _l_(674302)

    _c_(674300, _a_(674299, _c_(674298, _n_(674297, "MyApp", lambda: MyApp)), "run"))
    _l_(674301)

_c_(674305, _a_(674304, _n_(674303, "conn", lambda: conn), "close"))
_l_(674306)