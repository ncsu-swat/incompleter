# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68352395/attributeerror-super-object-has-no-attribute-getattr-in-python-and-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(558276)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(558278)

except ImportError:
    pass
try:
    import mysql.connector as ms
    _l_(558280)

except ImportError:
    pass
try:
    from kivy.properties import StringProperty, NumericProperty
    _l_(558282)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(558284)

except ImportError:
    pass


acc = _c_(558286, _n_(558285, "NumericProperty", lambda: NumericProperty), "")
_l_(558287)
pw = _c_(558289, _n_(558288, "StringProperty", lambda: StringProperty), "")
_l_(558290)

class safarApp(_n_(558291, "MDApp", lambda: MDApp)):
    _l_(558344)

    def build(self):
        _l_(558299)

        _a_(558293, _n_(558292, "self", lambda: self), "theme_cls").theme_style = 'Dark'
        _l_(558294)
        _a_(558296, _n_(558295, "self", lambda: self), "theme_cls").primary_palette = 'BlueGray'
        _l_(558297)
        aux = ""
        _l_(558298)
        return aux
    def Login(self):
        _l_(558343)

        _n_(558300, "self", lambda: self).acc = _a_(558305, _a_(558304, _a_(558303, _a_(558302, _n_(558301, "self", lambda: self), "root"), "ids"), "acc_num"), "text")
        _l_(558306)
        
        _n_(558307, "self", lambda: self).pw = _a_(558312, _a_(558311, _a_(558310, _a_(558309, _n_(558308, "self", lambda: self), "root"), "ids"), "password"), "text")
        _l_(558313)
        
        host = _c_(558316, _a_(558315, _n_(558314, "ms", lambda: ms), "connect"), host="localhost",
          user="root",
          password="bhawarth20",
          database="safar"
          )
        _l_(558317)
          
        cur = _c_(558320, _a_(558319, _n_(558318, "host", lambda: host), "cursor"), buffered = True)
        _l_(558321)
        
        
        
        _c_(558328, _a_(558323, _n_(558322, "cur", lambda: cur), "execute"), "Select * from data where Account_Number = %s and Password = %s collate utf8mb4_bin", (_a_(558325, _n_(558324, "self", lambda: self), "acc"), _a_(558327, _n_(558326, "self", lambda: self), "pw")))
        _l_(558329)
        data="error" #initially just assign the value
        _l_(558330) #initially just assign the value
        
        for i in _n_(558331, "cur", lambda: cur):
            _l_(558342)

            data=_n_(558332, "i", lambda: i) #if cursor has no data then loop will not run and value of data will be 'error'
            _l_(558333) #if cursor has no data then loop will not run and value of data will be 'error'
            if _n_(558334, "data", lambda: data)== "error":
                _l_(558341)

                _c_(558336, _n_(558335, "print", lambda: print), "User Does not exist")
                _l_(558337)
            else:
                _c_(558339, _n_(558338, "print", lambda: print), "User exist")
                _l_(558340)

class LoginScreen(_n_(558345, "Screen", lambda: Screen)):
    _l_(558347)

    pass
    _l_(558346)
class SignUpScreen(_n_(558348, "Screen", lambda: Screen)):
    _l_(558350)

    pass
    _l_(558349)


sm = _c_(558352, _n_(558351, "ScreenManager", lambda: ScreenManager))
_l_(558353)
_c_(558358, _a_(558355, _n_(558354, "sm", lambda: sm), "add_widget"), _c_(558357, _n_(558356, "LoginScreen", lambda: LoginScreen), name= "login"))
_l_(558359)
_c_(558364, _a_(558361, _n_(558360, "sm", lambda: sm), "add_widget"), _c_(558363, _n_(558362, "SignUpScreen", lambda: SignUpScreen), name= "signup"))
_l_(558365)



                    
                    
if _n_(558366, "__name__", lambda: __name__) == '__main__':
    _l_(558372)

    _c_(558370, _a_(558369, _c_(558368, _n_(558367, "safarApp", lambda: safarApp)), "run"))
    _l_(558371)