# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65372742/python-kivy-attributeerror-nonetype-object-has-no-attribute-text
# main.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(634721)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(634723)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(634725)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(634727)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(634729)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(634731)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(634733)

except ImportError:
    pass
try:
    from kivymd.uix.list import MDList,OneLineListItem
    _l_(634735)

except ImportError:
    pass
try:
    from kivy.uix.scrollview import ScrollView
    _l_(634737)

except ImportError:
    pass
try:
    from exel import DataBase
    _l_(634739)

except ImportError:
    pass

class TOPRIGHTINVOICE(_n_(634740, "Screen", lambda: Screen)):
    _l_(634778)

    invoice = _c_(634742, _n_(634741, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(634743)
    For = _c_(634745, _n_(634744, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(634746)

    def next(self):
        _l_(634763)

        _c_(634755, _a_(634748, _n_(634747, "db", lambda: db), "add_loadinfo"), _a_(634751, _a_(634750, _n_(634749, "self", lambda: self), "invoice"), "text"), _a_(634754, _a_(634753, _n_(634752, "self", lambda: self), "For"), "text"))
        _l_(634756)

        _c_(634759, _a_(634758, _n_(634757, "self", lambda: self), "reset"))
        _l_(634760)
        _n_(634761, "sm", lambda: sm).current = "CARRIERPAGE"
        _l_(634762)
    
    def reset(self):
        _l_(634770)

        _a_(634765, _n_(634764, "self", lambda: self), "invoice").text = "" 
        _l_(634766) 
        _a_(634768, _n_(634767, "self", lambda: self), "For").text = ""
        _l_(634769)

    def login(self):
        _l_(634777)

        _c_(634773, _a_(634772, _n_(634771, "self", lambda: self), "reset"))
        _l_(634774)
        _n_(634775, "sm", lambda: sm).current = "CARRIERPAGE"
        _l_(634776)


class CARRIERPAGE(_n_(634779, "Screen", lambda: Screen)):
    _l_(634816)


    def build(self):
        _l_(634815)

        screen = _c_(634781, _n_(634780, "Screen", lambda: Screen))
        _l_(634782)

        scroll = _c_(634784, _n_(634783, "ScrollView", lambda: ScrollView))
        _l_(634785)
        list_view= _c_(634787, _n_(634786, "MDList", lambda: MDList))
        _l_(634788)
        _c_(634792, _a_(634790, _n_(634789, "scroll", lambda: scroll), "add_widget"), _n_(634791, "list_view", lambda: list_view))
        _l_(634793)

        item1 = _c_(634795, _n_(634794, "OneLineListItem", lambda: OneLineListItem), text='Coyote')
        _l_(634796)
        item2 = _c_(634798, _n_(634797, "OneLineListItem", lambda: OneLineListItem), text='TQL')
        _l_(634799)

        _c_(634803, _a_(634801, _n_(634800, "list_view", lambda: list_view), "add_widget"), _n_(634802, "item1", lambda: item1))
        _l_(634804)
        _c_(634808, _a_(634806, _n_(634805, "list_view", lambda: list_view), "add_widget"), _n_(634807, "item2", lambda: item2))
        _l_(634809)

        _c_(634813, _a_(634811, _n_(634810, "screen", lambda: screen), "add_widget"), _n_(634812, "list_view", lambda: list_view))
        _l_(634814)


def MissingInfo():
    _l_(634826)

    pop = _c_(634820, _n_(634817, "Popup", lambda: Popup), title= 'Missing Information',
                content=_c_(634819, _n_(634818, "Label", lambda: Label), text='You are missing information, are you sure you want to continue?'),
                suze_hint=(None,None), size=(400,400))
    _l_(634821)
    _c_(634824, _a_(634823, _n_(634822, "pop", lambda: pop), "open"))
    _l_(634825)

class WindowManager(_n_(634827, "ScreenManager", lambda: ScreenManager)):
    _l_(634829)

    pass
    _l_(634828)

kv = _c_(634832, _a_(634831, _n_(634830, "Builder", lambda: Builder), "load_file"), "my.kv")
_l_(634833)

sm = _c_(634835, _n_(634834, "WindowManager", lambda: WindowManager))
_l_(634836)
db = _c_(634838, _n_(634837, "DataBase", lambda: DataBase), "user.txt")
_l_(634839)

screens = [_c_(634841, _n_(634840, "TOPRIGHTINVOICE", lambda: TOPRIGHTINVOICE), name="main"), _c_(634843, _n_(634842, "CARRIERPAGE", lambda: CARRIERPAGE), name="CARRIERPAGE")]
_l_(634844)
for screen in _n_(634845, "screens", lambda: screens):
    _l_(634851)

    _c_(634849, _a_(634847, _n_(634846, "sm", lambda: sm), "add_widget"), _n_(634848, "screen", lambda: screen))
    _l_(634850)

_n_(634852, "sm", lambda: sm).current = "main"
_l_(634853)

class MyScreen(_n_(634854, "App", lambda: App)):
    _l_(634858)

    def build(self):
        _l_(634857)

        aux = _n_(634855, "sm", lambda: sm)
        _l_(634856)
        return aux

if _n_(634859, "__name__", lambda: __name__) == "__main__":
    _l_(634865)

    _c_(634863, _a_(634862, _c_(634861, _n_(634860, "MyScreen", lambda: MyScreen)), "run"))
    _l_(634864)