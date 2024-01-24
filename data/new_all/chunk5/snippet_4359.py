# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59201728/having-a-problem-with-the-kivy-attribute-error-how-to-fix-attributeerror-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(668482)

except ImportError:
    pass
try:
    from kivy.factory import Factory
    _l_(668484)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(668486)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(668488)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(668490)

except ImportError:
    pass
_c_(668493, _a_(668492, _n_(668491, "Builder", lambda: Builder), "load_file"), 'signin/sign.kv')
_l_(668494)

class LoginScreen(_n_(668495, "BoxLayout", lambda: BoxLayout)):
    _l_(668527)


    def validate_user(self):
        _l_(668526)

        user = _a_(668498, _a_(668497, _n_(668496, "self", lambda: self), "ids"), "email_field")
        _l_(668499)
        pwd = _a_(668502, _a_(668501, _n_(668500, "self", lambda: self), "ids"), "pwd_field")
        _l_(668503)
        info = _a_(668506, _a_(668505, _n_(668504, "self", lambda: self), "ids"), "info")
        _l_(668507)

        uname = _a_(668509, _n_(668508, "user", lambda: user), "text")
        _l_(668510)
        passw = _a_(668512, _n_(668511, "pwd", lambda: pwd), "text")
        _l_(668513)

        if _n_(668514, "uname", lambda: uname) == '' or _n_(668515, "passw", lambda: passw) =='':
            _l_(668525)

            _n_(668516, "info", lambda: info).text = '[color=#FF0000]username and/ or password required[/color]'
            _l_(668517)
        else:
            if _n_(668518, "uname", lambda: uname) == 'admin' and _n_(668519, "passw", lambda: passw) == 'admin':
                _l_(668524)

                _n_(668520, "info", lambda: info).text = '[color=#00FF00]Logged In Succesfully!![/color]'
                _l_(668521)
            else:
                _n_(668522, "info", lambda: info).text = '[color=#FF0000]Invalid Username and/ or Password[/color]'
                _l_(668523)

class SignApp(_n_(668528, "MDApp", lambda: MDApp)):
    _l_(668545)

    title = "LOGIN SCREEN"
    _l_(668529)

    def build(self):
        _l_(668533)

        aux = _c_(668531, _n_(668530, "LoginScreen", lambda: LoginScreen))
        _l_(668532)
        return aux



    def show_password(self, field, button):
        _l_(668544)

        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        _n_(668534, "field", lambda: field).password = not _a_(668536, _n_(668535, "field", lambda: field), "password")
        _l_(668537)
        _n_(668538, "field", lambda: field).focus = True
        _l_(668539)
        _n_(668540, "button", lambda: button).icon = 'eye' if _a_(668542, _n_(668541, "button", lambda: button), "icon") == 'eye-off' else 'eye-off'
        _l_(668543)


if _n_(668546, "__name__", lambda: __name__) == '__main__':
    _l_(668554)

    sa = _c_(668548, _n_(668547, "SignApp", lambda: SignApp))
    _l_(668549)
    _c_(668552, _a_(668551, _n_(668550, "sa", lambda: sa), "run"))
    _l_(668553)