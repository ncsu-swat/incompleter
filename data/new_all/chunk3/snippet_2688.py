# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66800565/attributeerror-screen-object-has-no-attribute-text-in-python-kivymd
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(531245)

except ImportError:
    pass
try:
    from kivymd.uix.screen import Screen
    _l_(531247)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(531249)

except ImportError:
    pass
try:
    from kivymd.uix.menu import MDDropdownMenu
    _l_(531251)

except ImportError:
    pass
try:
    from kivymd.uix.chip import MDChip
    _l_(531253)

except ImportError:
    pass
try:
    from kivymd.uix.floatlayout import FloatLayout
    _l_(531255)

except ImportError:
    pass

button = '''
Screen:
    MDRaisedButton:
        id: button_id
        text: "PRESS ME"
        pos_hint: {"center_x": .35, "center_y": .8}
        on_release: app.drop.open()
'''
_l_(531256)

button1 = '''
Screen:
    MDRaisedButton:
        id: button1_id
        text: "PRESS ME 2"
        pos_hint: {"center_x": .5, "center_y": .8}
        on_release: app.clear()
'''
_l_(531257)

list1 = (['Item 1','Item 2','Item 3'], ['Item 4', 'Item 5', 'Item 6'])
_l_(531258)
class Test(_n_(531259, "MDApp", lambda: MDApp)):
    _l_(531343)

    def build(self):
        _l_(531308)

        _n_(531260, "self", lambda: self).screen = _c_(531262, _n_(531261, "Screen", lambda: Screen))
        _l_(531263)
        _n_(531264, "self", lambda: self).btn = _c_(531268, _a_(531266, _n_(531265, "Builder", lambda: Builder), "load_string"), _n_(531267, "button", lambda: button))
        _l_(531269)
        _n_(531270, "self", lambda: self).btn1 = _c_(531274, _a_(531272, _n_(531271, "Builder", lambda: Builder), "load_string"), _n_(531273, "button1", lambda: button1))
        _l_(531275)

        _c_(531281, _a_(531278, _a_(531277, _n_(531276, "self", lambda: self), "screen"), "add_widget"), _a_(531280, _n_(531279, "self", lambda: self), "btn1"))
        _l_(531282)
        _c_(531288, _a_(531285, _a_(531284, _n_(531283, "self", lambda: self), "screen"), "add_widget"), _a_(531287, _n_(531286, "self", lambda: self), "btn"))
        _l_(531289)


        _n_(531290, "self", lambda: self).drop = _c_(531296, _n_(531291, "MDDropdownMenu", lambda: MDDropdownMenu), caller = _a_(531295, _a_(531294, _a_(531293, _n_(531292, "self", lambda: self), "btn"), "ids"), "button_id"),
            items = [{'text':'Show Chips'}],
            width_mult = 4,
        )
        _l_(531297)
        _c_(531303, _a_(531300, _a_(531299, _n_(531298, "self", lambda: self), "drop"), "bind"), on_release=_a_(531302, _n_(531301, "self", lambda: self), "testing"))
        _l_(531304)
        aux = _a_(531306, _n_(531305, "self", lambda: self), "screen")
        _l_(531307)

        return aux
    
    def testing(self, menu, menu_item):
        _l_(531327)

        objects = {0.2 : "Item 1", 0.5 : "Item 2", 0.8 : "Item 3"}
        _l_(531309)
        for pos, item in _c_(531312, _a_(531311, _n_(531310, "objects", lambda: objects), "items")):
            _l_(531326)

            _n_(531313, "self", lambda: self).chip = _c_(531317, _n_(531314, "MDChip", lambda: MDChip), text = _n_(531315, "item", lambda: item),
                check = True,
                pos_hint = {"center_x":_n_(531316, "pos", lambda: pos), "center_y":0.4},
                
            )
            _l_(531318)
            _c_(531324, _a_(531321, _a_(531320, _n_(531319, "self", lambda: self), "screen"), "add_widget"), _a_(531323, _n_(531322, "self", lambda: self), "chip"))
            _l_(531325)

    def clear(self):
        _l_(531342)

        for child in _a_(531330, _a_(531329, _n_(531328, "self", lambda: self), "root"), "children")[:]:
            _l_(531341)

            if _a_(531332, _n_(531331, "child", lambda: child), "text") in _n_(531333, "list1", lambda: list1)[0]:
                _l_(531340)

                _c_(531338, _a_(531336, _a_(531335, _n_(531334, "self", lambda: self), "root"), "remove_widget"), _n_(531337, "child", lambda: child))
                _l_(531339)

_c_(531347, _a_(531346, _c_(531345, _n_(531344, "Test", lambda: Test)), "run"))
_l_(531348)