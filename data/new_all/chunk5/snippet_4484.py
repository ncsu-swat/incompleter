# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56824210/typeerror-nonetype-object-is-not-subscriptable-kivy-package-problem
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(659460)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(659462)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(659464)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(659466)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(659468)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(659470)

except ImportError:
    pass
try:
    import sqlite3
    _l_(659472)

except ImportError:
    pass

conn = _c_(659475, _a_(659474, _n_(659473, "sqlite3", lambda: sqlite3), "connect"), ":memory:")
_l_(659476)
cur = _c_(659479, _a_(659478, _n_(659477, "conn", lambda: conn), "cursor"))
_l_(659480)

_c_(659483, _a_(659482, _n_(659481, "cur", lambda: cur), "execute"), """CREATE TABLE votes (email NOT NULL, password NOT NULL, votes_yes INTEGER, votes_no INTEGER)""")
_l_(659484)


class LoginWindow(_n_(659485, "Screen", lambda: Screen)):
    _l_(659521)

    email = _c_(659487, _n_(659486, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(659488)
    password = _c_(659490, _n_(659489, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(659491)

    def login(self):
        _l_(659513)

        with _n_(659492, "conn", lambda: conn):
            _l_(659512)

            _c_(659495, _a_(659494, _n_(659493, "cur", lambda: cur), "execute"), "SELECT * FROM votes WHERE email = ? And password = ?, (self.email.text, self.password.text)")
            _l_(659496)
            result = _c_(659499, _a_(659498, _n_(659497, "cur", lambda: cur), "fetchone"))
            _l_(659500)
            if _n_(659501, "result", lambda: result):
                _l_(659511)

                _c_(659504, _a_(659503, _n_(659502, "self", lambda: self), "reset"))
                _l_(659505)
                _n_(659506, "sm", lambda: sm).current = "voting"
                _l_(659507)
            else:
                _c_(659509, _n_(659508, "invalid_login", lambda: invalid_login))
                _l_(659510)

    def reset(self):
        _l_(659520)

        _a_(659515, _n_(659514, "self", lambda: self), "email").text = ""
        _l_(659516)
        _a_(659518, _n_(659517, "self", lambda: self), "password").text = ""
        _l_(659519)


class VotingWindow(_n_(659522, "Screen", lambda: Screen)):
    _l_(659540)

    email = _c_(659524, _n_(659523, "ObjectProperty", lambda: ObjectProperty))
    _l_(659525)

    def yes_btn(self):
        _l_(659532)

        with _n_(659526, "conn", lambda: conn):
            _l_(659531)

            _c_(659529, _a_(659528, _n_(659527, "cur", lambda: cur), "execute"), "UPDATE votes set vote_yes = 1 WHERE email = self.email.text")
            _l_(659530)

    def no_btn(self):
        _l_(659539)

        with _n_(659533, "conn", lambda: conn):
            _l_(659538)

            _c_(659536, _a_(659535, _n_(659534, "cur", lambda: cur), "execute"), "UPDATE votes set vote_no = 1 WHERE email = self.email.text")
            _l_(659537)


class CreateAccountWindow(_n_(659541, "Screen", lambda: Screen)):
    _l_(659575)

    email = _c_(659543, _n_(659542, "ObjectProperty", lambda: ObjectProperty))
    _l_(659544)
    password = _c_(659546, _n_(659545, "ObjectProperty", lambda: ObjectProperty))
    _l_(659547)

    def create_btn(self):
        _l_(659567)

        with _n_(659548, "conn", lambda: conn):
            _l_(659566)

            results = _c_(659551, _a_(659550, _n_(659549, "cur", lambda: cur), "execute"), "SELECT * FROM votes WHERE email = ?, (self.email.text,)")
            _l_(659552)
            if _n_(659553, "results", lambda: results):
                _l_(659565)

                _c_(659555, _n_(659554, "invalid_form", lambda: invalid_form))
                _l_(659556)
            else:
                _c_(659559, _a_(659558, _n_(659557, "cur", lambda: cur), "execute"), "INSERT into votes VALUES(email = ?, password = ?), (self.email.text, self.password.text)")
                _l_(659560)
                _c_(659563, _a_(659562, _n_(659561, "self", lambda: self), "reset"))
                _l_(659564)

    def reset(self):
        _l_(659574)

        _a_(659569, _n_(659568, "self", lambda: self), "email").text = ""
        _l_(659570)
        _a_(659572, _n_(659571, "self", lambda: self), "password").text = ""
        _l_(659573)


class WindowManager(_n_(659576, "ScreenManager", lambda: ScreenManager)):
    _l_(659578)

    pass
    _l_(659577)


def invalid_login():
    _l_(659588)

    pop = _c_(659582, _n_(659579, "Popup", lambda: Popup), title='Invalid Login',
                  content=_c_(659581, _n_(659580, "Label", lambda: Label), text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    _l_(659583)
    _c_(659586, _a_(659585, _n_(659584, "pop", lambda: pop), "open"))
    _l_(659587)

def invalid_form():
    _l_(659598)

    pop = _c_(659592, _n_(659589, "Popup", lambda: Popup), title='Error',
                  content=_c_(659591, _n_(659590, "Label", lambda: Label), text='An account already exists with that email address'),
                  size_hint=(None, None), size=(400, 400))
    _l_(659593)
    _c_(659596, _a_(659595, _n_(659594, "pop", lambda: pop), "open"))
    _l_(659597)


kv = _c_(659601, _a_(659600, _n_(659599, "Builder", lambda: Builder), "load_file"), "my.kv")
_l_(659602)
sm = _c_(659604, _n_(659603, "WindowManager", lambda: WindowManager))
_l_(659605)

screens = [_c_(659607, _n_(659606, "LoginWindow", lambda: LoginWindow), name="login"), _c_(659609, _n_(659608, "CreateAccountWindow", lambda: CreateAccountWindow), name="create account"), _c_(659611, _n_(659610, "VotingWindow", lambda: VotingWindow), name="voting")]
_l_(659612)
for screen in _n_(659613, "screens", lambda: screens):
    _l_(659619)

    _c_(659617, _a_(659615, _n_(659614, "sm", lambda: sm), "add_widget"), _n_(659616, "screen", lambda: screen))
    _l_(659618)

_n_(659620, "sm", lambda: sm).current = "login"
_l_(659621)


class MyApp(_n_(659622, "App", lambda: App)):
    _l_(659626)

    def build(self):
        _l_(659625)

        aux = _n_(659623, "sm", lambda: sm)
        _l_(659624)
        return aux


if _n_(659627, "__name__", lambda: __name__) == '__main__':
    _l_(659633)

    _c_(659631, _a_(659630, _c_(659629, _n_(659628, "MyApp", lambda: MyApp)), "run"))
    _l_(659632)

_c_(659636, _a_(659635, _n_(659634, "conn", lambda: conn), "close"))
_l_(659637)