# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64229421/attributeerror-super-object-has-no-attribute-getattr-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserHomeScrren(_n_(553336, "BoxLayout", lambda: BoxLayout)):
    _l_(553412)

    

    def __init__(self, **kwargs):
        _l_(553344)

        _c_(553342, _a_(553340, _n_(553337, "super", lambda: super)(_n_(553338, "UserHomeScrren", lambda: UserHomeScrren), _n_(553339, "self", lambda: self)), "__init__"), **_n_(553341, "kwargs", lambda: kwargs))
        _l_(553343)
     

    def calculate(self):
        _l_(553391)

        #weight =int(self.weight.text)
        weight=_c_(553354, _n_(553345, "int", lambda: int), _a_(553353, _a_(553352, _a_(553351, _a_(553350, _a_(553349, _a_(553348, _a_(553347, _n_(553346, "self", lambda: self), "ids"), "backdrop"), "ids"), "backlayer"), "bmi_screen"), "weight"), "text"))
        _l_(553355)
        height= _c_(553365, _n_(553356, "int", lambda: int), _a_(553364, _a_(553363, _a_(553362, _a_(553361, _a_(553360, _a_(553359, _a_(553358, _n_(553357, "self", lambda: self), "ids"), "backdrop"), "ids"), "backlayer"), "bmi_screen"), "height"), "text"))
        _l_(553366)
        _c_(553375, _n_(553367, "print", lambda: print), _a_(553374, _a_(553373, _a_(553372, _a_(553371, _a_(553370, _a_(553369, _n_(553368, "self", lambda: self), "ids"), "backlayer"), "ids"), "bmi_screen"), "ids"), "height"))
        _l_(553376)
        BMI = _c_(553380, _n_(553377, "round", lambda: round), (_n_(553378, "weight", lambda: weight) * 703) / (_n_(553379, "height", lambda: height) ** 2))
        _l_(553381)

        if _n_(553382, "BMI", lambda: BMI) < 18.5:
            _l_(553390)

            _a_(553385, _a_(553384, _n_(553383, "self", lambda: self), "ids"), "results").text += "Your BMI is " + _c_(553388, _n_(553386, "str", lambda: str), _n_(553387, "BMI", lambda: BMI)) + " which means you are underweight."
            _l_(553389)


    def clear(self):
        _l_(553411)

        _a_(553394, _a_(553393, _n_(553392, "self", lambda: self), "ids"), "results").text = ""
        _l_(553395)
        _a_(553398, _a_(553397, _n_(553396, "self", lambda: self), "ids"), "weight").text = ""
        _l_(553399)
        _a_(553402, _a_(553401, _n_(553400, "self", lambda: self), "ids"), "height").text = ""
        _l_(553403)
        

        _c_(553406, _n_(553404, "print", lambda: print), _n_(553405, "weight", lambda: weight))
        _l_(553407)
        _c_(553409, _n_(553408, "print", lambda: print), 'calculate.....')
        _l_(553410)


class ItemBackdropBackLayer(_n_(553413, "ThemableBehavior", lambda: ThemableBehavior), _n_(553414, "BoxLayout", lambda: BoxLayout)):
    _l_(553446)

    icon = _c_(553415, StringProperty, "android")
    _l_(553416)
    text = _c_(553417, StringProperty)
    _l_(553418)
    selected_item = _c_(553419, BooleanProperty, False)
    _l_(553420)

    def on_touch_down(self, touch):
        _l_(553445)

        if _c_(553427, _a_(553422, _n_(553421, "self", lambda: self), "collide_point"), _a_(553424, _n_(553423, "touch", lambda: touch), "x"), _a_(553426, _n_(553425, "touch", lambda: touch), "y")):
            _l_(553439)

            for item in _a_(553430, _a_(553429, _n_(553428, "self", lambda: self), "parent"), "children"):
                _l_(553436)

                if _a_(553432, _n_(553431, "item", lambda: item), "selected_item"):
                    _l_(553435)

                    _n_(553433, "item", lambda: item).selected_item = False
                    _l_(553434)
            _n_(553437, "self", lambda: self).selected_item = True
            _l_(553438)
        aux = _c_(553443, _a_(553441, _n_(553440, "super", lambda: super)(), "on_touch_down"), _n_(553442, "touch", lambda: touch))
        _l_(553444)
        return aux


class UserApp(_n_(553447, "MDApp", lambda: MDApp)):
    _l_(553471)

    def __init__(self, **kwargs):
        _l_(553460)

        _n_(553448, "self", lambda: self).title = "User Flana"
        _l_(553449)
        _a_(553451, _n_(553450, "self", lambda: self), "theme_cls").primary_palette = "DeepPurple"
        _l_(553452)
        _c_(553456, _a_(553454, _n_(553453, "super", lambda: super)(), "__init__"), **_n_(553455, "kwargs", lambda: kwargs))
        _l_(553457)
        _n_(553458, "Window", lambda: Window).size = (300, 550)
        _l_(553459)

    def __getattr__(self, attr):
        _l_(553466)

        aux = _c_(553464, _a_(553462, _n_(553461, "super", lambda: super)(), "__getattr__"), _n_(553463, "attr", lambda: attr))
        _l_(553465)
        return aux

    def build(self):
        _l_(553470)

        aux = _c_(553468, _n_(553467, "UserHomeScrren", lambda: UserHomeScrren))
        _l_(553469)
        return aux
if _n_(553472, "__name__", lambda: __name__) == "__main__":
    _l_(553478)

    _c_(553476, _a_(553475, _c_(553474, _n_(553473, "UserApp", lambda: UserApp)), "run"))
    _l_(553477)