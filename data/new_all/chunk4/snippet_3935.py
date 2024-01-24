# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65171375/kivymd-get-attribute-error-from-textfield-python3-kivymd
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(643742)

except ImportError:
    pass
try:
    from kivy.lang.builder import Builder
    _l_(643744)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(643746)

except ImportError:
    pass

KV = """
ScreenManager:
    MainScreen:
    LoginScreen:
    RegisterScreen:
<MainScreen>:
    name: 'main'
    MDLabel:
        text:"Çetele"
        font_style:"H3"
        pos_hint:{'center_x':0.5,'center_y':0.94}
    MDRectangleFlatButton:
        text: 'Giriş Yap'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'login'
    MDRectangleFlatButton:
        text: 'Kayıt Ol'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'register'
    
<LoginScreen>:
    name: 'login'
    
    MDToolbar:
        title:"Çetele Giriş Yap"
        pos_hint: {'top':1}

    MDTextField:
        id:'email'
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.6}
        hint_text:"E-Mail"
        helper_text: "E-Mail"

    MDTextField:
        name:"password"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.5}
        hint_text:"Şifre"
        helper_text: "E-Mail"


    MDRectangleFlatButton:
        text:"Contiune"
        on_release: app.Login()



    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'center_x':0.09,'center_y':0.1}
        on_press: root.manager.current = 'main'
        





<RegisterScreen>:
    name: 'register'
    MDToolbar:
        title:"Çetele - Kayıt ol"
        pos_hint:{'top':1}
    MDTextField:
        name:"email"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.6}
        hint_text:"E-Mail"
        helper_text: "E-Mail"

    MDTextField:
        name:"password"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.5}
        hint_text:"Şifre"
        helper_text: "E-Mail"


    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'center_x':0.09,'center_y':0.1}
        on_press: root.manager.current = 'main'
        
"""
_l_(643747)


class MainScreen(_n_(643748, "Screen", lambda: Screen)):
    _l_(643750)

    pass
    _l_(643749)


class LoginScreen(_n_(643751, "Screen", lambda: Screen)):
    _l_(643753)

    pass
    _l_(643752)


class RegisterScreen(_n_(643754, "Screen", lambda: Screen)):
    _l_(643756)

    pass
    _l_(643755)


# Create the screen manager
sm = _c_(643758, _n_(643757, "ScreenManager", lambda: ScreenManager))
_l_(643759)
_c_(643764, _a_(643761, _n_(643760, "sm", lambda: sm), "add_widget"), _c_(643763, _n_(643762, "MainScreen", lambda: MainScreen), name='main'))
_l_(643765)
_c_(643770, _a_(643767, _n_(643766, "sm", lambda: sm), "add_widget"), _c_(643769, _n_(643768, "LoginScreen", lambda: LoginScreen), name='login'))
_l_(643771)
_c_(643776, _a_(643773, _n_(643772, "sm", lambda: sm), "add_widget"), _c_(643775, _n_(643774, "RegisterScreen", lambda: RegisterScreen), name='register'))
_l_(643777)


class DemoApp(_n_(643778, "MDApp", lambda: MDApp)):
    _l_(643804)

    
    def build(self):
        _l_(643794)

        _a_(643780, _n_(643779, "self", lambda: self), "theme_cls").primary_palette = "Blue"
        _l_(643781)
        _a_(643783, _n_(643782, "self", lambda: self), "theme_cls").primary_hue = "A700"
        _l_(643784)
        _n_(643785, "self", lambda: self).screen = _c_(643789, _a_(643787, _n_(643786, "Builder", lambda: Builder), "load_string"), _n_(643788, "KV", lambda: KV))
        _l_(643790)
        aux = _a_(643792, _n_(643791, "self", lambda: self), "screen")
        _l_(643793)

        return aux
    def Login(self):
        _l_(643803)

        text = _a_(643797, _a_(643796, _n_(643795, "self", lambda: self), "root"), "ids")
        _l_(643798)
        _c_(643801, _n_(643799, "print", lambda: print), _n_(643800, "text", lambda: text))
        _l_(643802)

_c_(643808, _a_(643807, _c_(643806, _n_(643805, "DemoApp", lambda: DemoApp)), "run"))
_l_(643809)