# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59416972/python-kivy-attributeerror-nonetype-object-has-no-attribute-bind
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(572027)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(572029)

except ImportError:
    pass
try:
    from kivy.properties import ListProperty, NumericProperty, BooleanProperty, StringProperty
    _l_(572031)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(572033)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(572035)

except ImportError:
    pass
try:
    import calculator_calc
    _l_(572037)

except ImportError:
    pass




_c_(572040, _a_(572039, _n_(572038, "Builder", lambda: Builder), "load_file"), "calculatorgui.kv")
_l_(572041)



class CalculatorScreen1(_n_(572042, "Screen", lambda: Screen)):
    _l_(572044)

    pass
    _l_(572043)

class CalculatorScreen2(_n_(572045, "Screen", lambda: Screen)):
    _l_(572047)

    pass
    _l_(572046)



class CalculatorModeIndicator(_n_(572048, "BoxLayout", lambda: BoxLayout)):
    _l_(572050)

    pass
    _l_(572049)

class CalculatorMonitor1(_n_(572051, "BoxLayout", lambda: BoxLayout)):
    _l_(572053)

    pass
    _l_(572052)

class CalculatorButtons(_n_(572054, "BoxLayout", lambda: BoxLayout)):
    _l_(572056)

    pass
    _l_(572055)





screen_manager = _c_(572058, _n_(572057, "ScreenManager", lambda: ScreenManager))
_l_(572059)

_c_(572064, _a_(572061, _n_(572060, "screen_manager", lambda: screen_manager), "add_widget"), _c_(572063, _n_(572062, "CalculatorScreen1", lambda: CalculatorScreen1), name = "screen1"))
_l_(572065)
_c_(572070, _a_(572067, _n_(572066, "screen_manager", lambda: screen_manager), "add_widget"), _c_(572069, _n_(572068, "CalculatorScreen2", lambda: CalculatorScreen2), name = "screen2"))
_l_(572071)



class Calculator(_n_(572072, "App", lambda: App)):
    _l_(572161)

    expression_tokens = _c_(572074, _n_(572073, "ListProperty", lambda: ListProperty), [])
    _l_(572075)
    expression_value = _c_(572077, _n_(572076, "StringProperty", lambda: StringProperty), "")
    _l_(572078)
    angle_mode = _c_(572080, _n_(572079, "StringProperty", lambda: StringProperty), "degrees")
    _l_(572081)
    angle_mode_text = _c_(572083, _n_(572082, "StringProperty", lambda: StringProperty), "D")
    _l_(572084)
    button_mode = _c_(572086, _n_(572085, "NumericProperty", lambda: NumericProperty), 1)
    _l_(572087)
    button_mode_text = _c_(572089, _n_(572088, "StringProperty", lambda: StringProperty), "1ST")
    _l_(572090)
    store_mode = _c_(572092, _n_(572091, "BooleanProperty", lambda: BooleanProperty), False)
    _l_(572093)


    def build(self):
        _l_(572096)

        aux = _n_(572094, "screen_manager", lambda: screen_manager)
        _l_(572095)
        return aux


    def switch_screen(self, screen):
        _l_(572100)

        _n_(572097, "screen_manager", lambda: screen_manager).current = _n_(572098, "screen", lambda: screen)
        _l_(572099)

    def set_button_mode(self, button_mode):
        _l_(572116)

        _n_(572101, "self", lambda: self).button_mode = _n_(572102, "button_mode", lambda: button_mode)
        _l_(572103)

        if _n_(572104, "button_mode", lambda: button_mode) == 1:
            _l_(572115)

            _n_(572105, "self", lambda: self).button_mode_text = "1ST"
            _l_(572106)
        elif _n_(572107, "button_mode", lambda: button_mode) == 2:
            _l_(572114)

            _n_(572108, "self", lambda: self).button_mode_text = "2ND"
            _l_(572109)
        elif _n_(572110, "button_mode", lambda: button_mode) == 3:
            _l_(572113)

            _n_(572111, "self", lambda: self).button_mode_text = "3RD"  
            _l_(572112)  

    def set_angle_mode(self, angle_mode):
        _l_(572137)

        _c_(572120, _a_(572118, _n_(572117, "calculator_calc", lambda: calculator_calc), "evaluate"), f"angle_mode {_n_(572119, 'angle_mode', lambda: angle_mode)}") 
        _l_(572121) 

        _n_(572122, "self", lambda: self).angle_mode = _n_(572123, "angle_mode", lambda: angle_mode)
        _l_(572124)

        if _n_(572125, "angle_mode", lambda: angle_mode) == "degrees":
            _l_(572136)

            _n_(572126, "self", lambda: self).angle_mode_text = "D"
            _l_(572127)
        elif _n_(572128, "angle_mode", lambda: angle_mode) == "radians":
            _l_(572135)

            _n_(572129, "self", lambda: self).angle_mode_text = "R"
            _l_(572130)
        elif _n_(572131, "angle_mode", lambda: angle_mode) == "gradians":
            _l_(572134)

            _n_(572132, "self", lambda: self).angle_mode_text = "G"  
            _l_(572133)  

    def add_token(self, token):
        _l_(572144)

        _c_(572142, _a_(572140, _a_(572139, _n_(572138, "self", lambda: self), "expression_tokens"), "append"), _n_(572141, "token", lambda: token))
        _l_(572143)

    def calculate(self, expression):
        _l_(572160)

        result = _c_(572148, _a_(572146, _n_(572145, "calculator_calc", lambda: calculator_calc), "evaluate"), _n_(572147, "expression", lambda: expression))
        _l_(572149)
        _n_(572150, "self", lambda: self).expression_value = _c_(572153, _n_(572151, "str", lambda: str), _n_(572152, "result", lambda: result))
        _l_(572154)
        _c_(572158, _a_(572156, _n_(572155, "calculator_calc", lambda: calculator_calc), "evaluate"), f"ANS = {_n_(572157, 'result', lambda: result)}")
        _l_(572159)


_c_(572165, _a_(572164, _c_(572163, _n_(572162, "Calculator", lambda: Calculator)), "run"))
_l_(572166)