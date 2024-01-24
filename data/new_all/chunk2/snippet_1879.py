# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44275919/kivy-attributeerror-nonetype-object-has-no-attribute-bind-when-accessing-l
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(446062)

except ImportError:
    pass
_c_(446065, _a_(446064, _n_(446063, "kivy", lambda: kivy), "require"), '1.10.0')
_l_(446066)
try:
    from kivy.app import App
    _l_(446068)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(446070)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(446072)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(446074)

except ImportError:
    pass
try:
    from kivy.uix.scrollview import ScrollView
    _l_(446076)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(446078)

except ImportError:
    pass
try:
    from kivy.uix.floatlayout import FloatLayout
    _l_(446080)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(446082)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(446084)

except ImportError:
    pass
try:
    from snartoolsmod import *
    _l_(446086)

except ImportError:
    pass

_c_(446089, _a_(446088, _n_(446087, "Builder", lambda: Builder), "load_file"), "snartools.kv")
_l_(446090)

class DiningButton(_n_(446091, "Button", lambda: Button)):
    _l_(446093)

    pass
    _l_(446092)

class DirectionButton(_n_(446094, "Button", lambda: Button)):
    _l_(446096)

    pass
    _l_(446095)

class ItemButton(_n_(446097, "Button", lambda: Button)):
    _l_(446099)

    pass
    _l_(446098)

class SubmenuButton(_n_(446100, "Button", lambda: Button)):
    _l_(446102)

    pass
    _l_(446101)

class HomeScreen(_n_(446103, "Screen", lambda: Screen)):
    _l_(446105)

    pass
    _l_(446104)

class WhitmansMenu(_n_(446106, "Screen", lambda: Screen)):
    _l_(446180)


    def initialize_list(self):
        _l_(446117)

        itemList = _c_(446108, _n_(446107, "Menu", lambda: Menu), 'whitmans')
        _l_(446109)
        global allItems
        _l_(446110)
        allItems = _c_(446113, _a_(446112, _n_(446111, "itemList", lambda: itemList), "getCopy"))
        _l_(446114)
        aux = _n_(446115, "itemList", lambda: itemList)
        _l_(446116)
        return aux

    def modify_list(self, itemList, value, dish):
        _l_(446146)

        if _n_(446118, "value", lambda: value) == 'down':
            _l_(446145)

            for item in _n_(446119, "itemList", lambda: itemList):
                _l_(446131)

                if _n_(446120, "dish", lambda: dish) == _c_(446123, _a_(446122, _n_(446121, "item", lambda: item), "getDish")):
                    _l_(446130)

                    _c_(446127, _a_(446125, _n_(446124, "itemList", lambda: itemList), "remove"), _n_(446126, "item", lambda: item))
                    _l_(446128)
                    break
                    _l_(446129)
        else:
            for item in _n_(446132, "allItems", lambda: allItems):
                _l_(446144)

                if _n_(446133, "dish", lambda: dish) == _c_(446136, _a_(446135, _n_(446134, "item", lambda: item), "getDish")):
                    _l_(446143)

                    _c_(446140, _a_(446138, _n_(446137, "itemList", lambda: itemList), "append"), _n_(446139, "item", lambda: item))
                    _l_(446141)
                    break
                    _l_(446142)

    def modify_state(self, value, submenu, length):
        _l_(446179)

        if _n_(446147, "value", lambda: value) == 'down':
            _l_(446178)

            for i in _c_(446150, _n_(446148, "range", lambda: range), 1, _n_(446149, "length", lambda: length)+1):
                _l_(446162)

                button = _a_(446152, _n_(446151, "self", lambda: self), "ids")[_c_(446155, _n_(446153, "str", lambda: str), _n_(446154, "submenu", lambda: submenu))+'_item'+_c_(446158, _n_(446156, "str", lambda: str), _n_(446157, "i", lambda: i))]
                _l_(446159)
                _n_(446160, "button", lambda: button).state = 'down'
                _l_(446161)
        else:
            for i in _c_(446165, _n_(446163, "range", lambda: range), 1, _n_(446164, "length", lambda: length)+1):
                _l_(446177)

                button = _a_(446167, _n_(446166, "self", lambda: self), "ids")[_c_(446170, _n_(446168, "str", lambda: str), _n_(446169, "submenu", lambda: submenu))+'_item'+_c_(446173, _n_(446171, "str", lambda: str), _n_(446172, "i", lambda: i))]
                _l_(446174)
                _n_(446175, "button", lambda: button).state = 'normal'
                _l_(446176)

class ToolScreen(_n_(446181, "Screen", lambda: Screen)):
    _l_(446183)

    pass
    _l_(446182)

class ToolButton(_n_(446184, "Button", lambda: Button)):
    _l_(446186)

    pass
    _l_(446185)

class InstructionsLabel(_n_(446187, "Label", lambda: Label)):
    _l_(446189)

    pass
    _l_(446188)

class SubLabel(_n_(446190, "Label", lambda: Label)):
    _l_(446192)

    pass
    _l_(446191)

class LengthExact(_n_(446193, "Screen", lambda: Screen)):
    _l_(446197)


    def get_list(self, itemList):
        _l_(446196)

        aux = _n_(446194, "itemList", lambda: itemList)
        _l_(446195)
        return aux

class LengthRange(_n_(446198, "Screen", lambda: Screen)):
    _l_(446200)

    pass
    _l_(446199)

class PriceExact(_n_(446201, "Screen", lambda: Screen)):
    _l_(446203)

    pass
    _l_(446202)

class PriceRange(_n_(446204, "Screen", lambda: Screen)):
    _l_(446206)

    pass
    _l_(446205)

class MoreExact(_n_(446207, "Screen", lambda: Screen)):
    _l_(446209)

    pass
    _l_(446208)

class MoreRange(_n_(446210, "Screen", lambda: Screen)):
    _l_(446212)

    pass
    _l_(446211)

screen_manager = _c_(446214, _n_(446213, "ScreenManager", lambda: ScreenManager))
_l_(446215)
_c_(446220, _a_(446217, _n_(446216, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446219, _n_(446218, "HomeScreen", lambda: HomeScreen), name="home_screen"))
_l_(446221)
_c_(446226, _a_(446223, _n_(446222, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446225, _n_(446224, "WhitmansMenu", lambda: WhitmansMenu), name="whitmans_menu"))
_l_(446227)
_c_(446232, _a_(446229, _n_(446228, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446231, _n_(446230, "ToolScreen", lambda: ToolScreen), name="tool_screen"))
_l_(446233)
_c_(446238, _a_(446235, _n_(446234, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446237, _n_(446236, "LengthExact", lambda: LengthExact), name="length_exact"))
_l_(446239)
_c_(446244, _a_(446241, _n_(446240, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446243, _n_(446242, "LengthRange", lambda: LengthRange), name="length_range"))
_l_(446245)
_c_(446250, _a_(446247, _n_(446246, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446249, _n_(446248, "PriceExact", lambda: PriceExact), name="price_exact"))
_l_(446251)
_c_(446256, _a_(446253, _n_(446252, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446255, _n_(446254, "PriceRange", lambda: PriceRange), name="price_range"))
_l_(446257)
_c_(446262, _a_(446259, _n_(446258, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446261, _n_(446260, "MoreExact", lambda: MoreExact), name="more_exact"))
_l_(446263)
_c_(446268, _a_(446265, _n_(446264, "screen_manager", lambda: screen_manager), "add_widget"), _c_(446267, _n_(446266, "MoreRange", lambda: MoreRange), name="more_range"))
_l_(446269)

class SnartoolsApp(_n_(446270, "App", lambda: App)):
    _l_(446274)


    def build(self):
        _l_(446273)

        aux = _n_(446271, "screen_manager", lambda: screen_manager)
        _l_(446272)
        return aux

app = _c_(446276, _n_(446275, "SnartoolsApp", lambda: SnartoolsApp))
_l_(446277)
_c_(446280, _a_(446279, _n_(446278, "app", lambda: app), "run"))
_l_(446281)