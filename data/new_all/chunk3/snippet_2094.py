# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64563883/attributeerror-kivy-properties-objectproperty-object-has-no-attribute-add-wi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(576866)

except ImportError:
    pass
try:
    from kivy.lang.builder import Builder
    _l_(576868)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(576870)

except ImportError:
    pass
try:
    from kivymd.uix.list import MDList,ThreeLineListItem
    _l_(576872)

except ImportError:
    pass
try:
    from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
    _l_(576874)

except ImportError:
    pass
try:
    from kivymd.uix.dialog import MDDialog
    _l_(576876)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(576878)

except ImportError:
    pass

class MenuScreen(_n_(576879, "Screen", lambda: Screen)):
    _l_(576883)

    list11=_c_(576881, _n_(576880, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(576882)
class ProfileScreen(_n_(576884, "Screen", lambda: Screen)):
    _l_(576925)

    field1=_c_(576886, _n_(576885, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(576887)
    field2=_c_(576889, _n_(576888, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(576890)
    field3=_c_(576892, _n_(576891, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(576893)
    def but1(self):
        _l_(576924)

        _n_(576894, "self", lambda: self).but2=_c_(576896, _n_(576895, "MDRectangleFlatButton", lambda: MDRectangleFlatButton), text='remove')
        _l_(576897)
        if _a_(576900, _a_(576899, _n_(576898, "self", lambda: self), "field1"), "text")=="":
            _l_(576923)

            _n_(576901, "self", lambda: self).box=_c_(576903, _n_(576902, "MDDialog", lambda: MDDialog), title='Your Username  ',text='you need to add Title',size_hint=(0.93,0))
            _l_(576904)
            _c_(576908, _a_(576907, _a_(576906, _n_(576905, "self", lambda: self), "box"), "open"))
            _l_(576909)
        else:
            _c_(576921, _a_(576912, _a_(576911, _n_(576910, "MenuScreen", lambda: MenuScreen), "list1"), "add_widget"), _c_(576920, _n_(576913, "ThreeLineListItem", lambda: ThreeLineListItem), text=_a_(576915, _n_(576914, "self", lambda: self), "field1"),secondary_text=_a_(576917, _n_(576916, "self", lambda: self), "field2"),tertiary_text=_a_(576919, _n_(576918, "self", lambda: self), "field3")))
            _l_(576922)



sm = _c_(576927, _n_(576926, "ScreenManager", lambda: ScreenManager))
_l_(576928)
_c_(576933, _a_(576930, _n_(576929, "sm", lambda: sm), "add_widget"), _c_(576932, _n_(576931, "MenuScreen", lambda: MenuScreen), name='menu'))
_l_(576934)
_c_(576939, _a_(576936, _n_(576935, "sm", lambda: sm), "add_widget"), _c_(576938, _n_(576937, "ProfileScreen", lambda: ProfileScreen), name='profile'))
_l_(576940)

class DemoApp(_n_(576941, "MDApp", lambda: MDApp)):
    _l_(576950)

    def build(self):
        _l_(576949)

        screen = _c_(576945, _a_(576943, _n_(576942, "Builder", lambda: Builder), "load_string"), _n_(576944, "screen_helper", lambda: screen_helper))
        _l_(576946)
        aux = _n_(576947, "screen", lambda: screen)
        _l_(576948)
        return aux



_c_(576954, _a_(576953, _c_(576952, _n_(576951, "DemoApp", lambda: DemoApp)), "run"))
_l_(576955)