# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56824210/typeerror-nonetype-object-is-not-subscriptable-kivy-package-problem
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(693003)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(693005)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(693007)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(693009)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(693011)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(693013)

except ImportError:
    pass
try:
    import sqlite3
    _l_(693015)

except ImportError:
    pass

conn = _c_(693018, _a_(693017, _n_(693016, "sqlite3", lambda: sqlite3), "connect"), ":memory:")
_l_(693019)
cur = _c_(693022, _a_(693021, _n_(693020, "conn", lambda: conn), "cursor"))
_l_(693023)

_c_(693026, _a_(693025, _n_(693024, "cur", lambda: cur), "execute"), """CREATE TABLE votes (email NOT NULL, password NOT NULL, votes_yes INTEGER, votes_no INTEGER)""")
_l_(693027)


class LoginWindow(_n_(693028, "Screen", lambda: Screen)):
    _l_(693064)

    email = _c_(693030, _n_(693029, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(693031)
    password = _c_(693033, _n_(693032, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(693034)

    def login(self):
        _l_(693056)

        with _n_(693035, "conn", lambda: conn):
            _l_(693055)

            _c_(693038, _a_(693037, _n_(693036, "cur", lambda: cur), "execute"), "SELECT * FROM votes WHERE email = ? And password = ?, (self.email.text, self.password.text)")
            _l_(693039)
            result = _c_(693042, _a_(693041, _n_(693040, "cur", lambda: cur), "fetchone"))
            _l_(693043)
            if _n_(693044, "result", lambda: result):
                _l_(693054)

                _c_(693047, _a_(693046, _n_(693045, "self", lambda: self), "reset"))
                _l_(693048)
                _n_(693049, "sm", lambda: sm).current = "voting"
                _l_(693050)
            else:
                _c_(693052, _n_(693051, "invalid_login", lambda: invalid_login))
                _l_(693053)

    def reset(self):
        _l_(693063)

        _a_(693058, _n_(693057, "self", lambda: self), "email").text = ""
        _l_(693059)
        _a_(693061, _n_(693060, "self", lambda: self), "password").text = ""
        _l_(693062)


class VotingWindow(_n_(693065, "Screen", lambda: Screen)):
    _l_(693083)

    email = _c_(693067, _n_(693066, "ObjectProperty", lambda: ObjectProperty))
    _l_(693068)

    def yes_btn(self):
        _l_(693075)

        with _n_(693069, "conn", lambda: conn):
            _l_(693074)

            _c_(693072, _a_(693071, _n_(693070, "cur", lambda: cur), "execute"), "UPDATE votes set vote_yes = 1 WHERE email = self.email.text")
            _l_(693073)

    def no_btn(self):
        _l_(693082)

        with _n_(693076, "conn", lambda: conn):
            _l_(693081)

            _c_(693079, _a_(693078, _n_(693077, "cur", lambda: cur), "execute"), "UPDATE votes set vote_no = 1 WHERE email = self.email.text")
            _l_(693080)


class CreateAccountWindow(_n_(693084, "Screen", lambda: Screen)):
    _l_(693118)

    email = _c_(693086, _n_(693085, "ObjectProperty", lambda: ObjectProperty))
    _l_(693087)
    password = _c_(693089, _n_(693088, "ObjectProperty", lambda: ObjectProperty))
    _l_(693090)

    def create_btn(self):
        _l_(693110)

        with _n_(693091, "conn", lambda: conn):
            _l_(693109)

            results = _c_(693094, _a_(693093, _n_(693092, "cur", lambda: cur), "execute"), "SELECT * FROM votes WHERE email = ?, (self.email.text,)")
            _l_(693095)
            if _n_(693096, "results", lambda: results):
                _l_(693108)

                _c_(693098, _n_(693097, "invalid_form", lambda: invalid_form))
                _l_(693099)
            else:
                _c_(693102, _a_(693101, _n_(693100, "cur", lambda: cur), "execute"), "INSERT into votes VALUES(email = ?, password = ?), (self.email.text, self.password.text)")
                _l_(693103)
                _c_(693106, _a_(693105, _n_(693104, "self", lambda: self), "reset"))
                _l_(693107)

    def reset(self):
        _l_(693117)

        _a_(693112, _n_(693111, "self", lambda: self), "email").text = ""
        _l_(693113)
        _a_(693115, _n_(693114, "self", lambda: self), "password").text = ""
        _l_(693116)


class WindowManager(_n_(693119, "ScreenManager", lambda: ScreenManager)):
    _l_(693121)

    pass
    _l_(693120)


def invalid_login():
    _l_(693131)

    pop = _c_(693125, _n_(693122, "Popup", lambda: Popup), title='Invalid Login',
                  content=_c_(693124, _n_(693123, "Label", lambda: Label), text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    _l_(693126)
    _c_(693129, _a_(693128, _n_(693127, "pop", lambda: pop), "open"))
    _l_(693130)

def invalid_form():
    _l_(693141)

    pop = _c_(693135, _n_(693132, "Popup", lambda: Popup), title='Error',
                  content=_c_(693134, _n_(693133, "Label", lambda: Label), text='An account already exists with that email address'),
                  size_hint=(None, None), size=(400, 400))
    _l_(693136)
    _c_(693139, _a_(693138, _n_(693137, "pop", lambda: pop), "open"))
    _l_(693140)


kv = _c_(693144, _a_(693143, _n_(693142, "Builder", lambda: Builder), "load_file"), "my.kv")
_l_(693145)
sm = _c_(693147, _n_(693146, "WindowManager", lambda: WindowManager))
_l_(693148)

screens = [_c_(693150, _n_(693149, "LoginWindow", lambda: LoginWindow), name="login"), _c_(693152, _n_(693151, "CreateAccountWindow", lambda: CreateAccountWindow), name="create account"), _c_(693154, _n_(693153, "VotingWindow", lambda: VotingWindow), name="voting")]
_l_(693155)
for screen in _n_(693156, "screens", lambda: screens):
    _l_(693162)

    _c_(693160, _a_(693158, _n_(693157, "sm", lambda: sm), "add_widget"), _n_(693159, "screen", lambda: screen))
    _l_(693161)

_n_(693163, "sm", lambda: sm).current = "login"
_l_(693164)


class MyApp(_n_(693165, "App", lambda: App)):
    _l_(693169)

    def build(self):
        _l_(693168)

        aux = _n_(693166, "sm", lambda: sm)
        _l_(693167)
        return aux


if _n_(693170, "__name__", lambda: __name__) == '__main__':
    _l_(693176)

    _c_(693174, _a_(693173, _c_(693172, _n_(693171, "MyApp", lambda: MyApp)), "run"))
    _l_(693175)

_c_(693179, _a_(693178, _n_(693177, "conn", lambda: conn), "close"))
_l_(693180)