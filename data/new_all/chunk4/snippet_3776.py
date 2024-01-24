# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68240266/kivy-event-eventdispatcher-init-is-raising-the-error-typeerror-object-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(643966)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(643968)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(643970)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(643972)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(643974)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(643976)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(643978)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(643980)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(643982)

except ImportError:
    pass


class LoginScreen(_n_(643983, "Widget", lambda: Widget)):
    _l_(643985)

    pass
    _l_(643984)

class PasswordScreen(_n_(643986, "Widget", lambda: Widget)):
    _l_(643988)

    pass
    _l_(643987)

class PasswordApp(_n_(643989, "App", lambda: App)):
    _l_(644008)

    def build(self):
        _l_(644007)

        sm = _c_(643991, _n_(643990, "ScreenManager", lambda: ScreenManager))
        _l_(643992)
        _c_(643997, _a_(643994, _n_(643993, "sm", lambda: sm), "add_widget"), _c_(643996, _n_(643995, "LoginScreen", lambda: LoginScreen), name='login'))
        _l_(643998)
        _c_(644003, _a_(644000, _n_(643999, "sm", lambda: sm), "add_widget"), _c_(644002, _n_(644001, "PasswordScreen", lambda: PasswordScreen), name='passwords'))
        _l_(644004)
        aux = _n_(644005, "sm", lambda: sm)
        _l_(644006)

        return aux

if _n_(644009, "__name__", lambda: __name__) == '__main__':
    _l_(644015)

    _c_(644013, _a_(644012, _c_(644011, _n_(644010, "PasswordApp", lambda: PasswordApp)), "run"))
    _l_(644014)