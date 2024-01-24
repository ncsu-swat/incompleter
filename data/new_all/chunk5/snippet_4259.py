# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59201728/having-a-problem-with-the-kivy-attribute-error-how-to-fix-attributeerror-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(668027)

except ImportError:
    pass
try:
    from kivy.factory import Factory
    _l_(668029)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(668031)

except ImportError:
    pass
try:
    from kivymd.theming import ThemeManager
    _l_(668033)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(668035)

except ImportError:
    pass
_c_(668038, _a_(668037, _n_(668036, "Builder", lambda: Builder), "load_file"), 'signin/sign.kv')
_l_(668039)

class LoginScreen(_n_(668040, "BoxLayout", lambda: BoxLayout)):
    _l_(668072)


    def validate_user(self):
        _l_(668071)

        user = _a_(668043, _a_(668042, _n_(668041, "self", lambda: self), "ids"), "email_field")
        _l_(668044)
        pwd = _a_(668047, _a_(668046, _n_(668045, "self", lambda: self), "ids"), "pwd_field")
        _l_(668048)
        info = _a_(668051, _a_(668050, _n_(668049, "self", lambda: self), "ids"), "info")
        _l_(668052)

        uname = _a_(668054, _n_(668053, "user", lambda: user), "text")
        _l_(668055)
        passw = _a_(668057, _n_(668056, "pwd", lambda: pwd), "text")
        _l_(668058)

        if _n_(668059, "uname", lambda: uname) == '' or _n_(668060, "passw", lambda: passw) =='':
            _l_(668070)

            _n_(668061, "info", lambda: info).text = '[color=#FF0000]username and/ or password required[/color]'
            _l_(668062)
        else:
            if _n_(668063, "uname", lambda: uname) == 'admin' and _n_(668064, "passw", lambda: passw) == 'admin':
                _l_(668069)

                _n_(668065, "info", lambda: info).text = '[color=#00FF00]Logged In Succesfully!![/color]'
                _l_(668066)
            else:
                _n_(668067, "info", lambda: info).text = '[color=#FF0000]Invalid Username and/ or Password[/color]'
                _l_(668068)

class SignApp(_n_(668073, "MDApp", lambda: MDApp)):
    _l_(668090)

    title = "LOGIN SCREEN"
    _l_(668074)

    def build(self):
        _l_(668078)

        aux = _c_(668076, _n_(668075, "LoginScreen", lambda: LoginScreen))
        _l_(668077)
        return aux



    def show_password(self, field, button):
        _l_(668089)

        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        _n_(668079, "field", lambda: field).password = not _a_(668081, _n_(668080, "field", lambda: field), "password")
        _l_(668082)
        _n_(668083, "field", lambda: field).focus = True
        _l_(668084)
        _n_(668085, "button", lambda: button).icon = 'eye' if _a_(668087, _n_(668086, "button", lambda: button), "icon") == 'eye-off' else 'eye-off'
        _l_(668088)


if _n_(668091, "__name__", lambda: __name__) == '__main__':
    _l_(668099)

    sa = _c_(668093, _n_(668092, "SignApp", lambda: SignApp))
    _l_(668094)
    _c_(668097, _a_(668096, _n_(668095, "sa", lambda: sa), "run"))
    _l_(668098)