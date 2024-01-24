# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60388935/trying-my-best-to-understand-this-attributeerror-nonetype-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivymd
    _l_(672344)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(672346)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(672348)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(672350)

except ImportError:
    pass
try:
    from kivymd.uix.textfield import MDTextField
    _l_(672352)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(672354)

except ImportError:
    pass


class MainApp(_n_(672355, "MDApp", lambda: MDApp)):
    _l_(672436)


    height_feet = _c_(672357, _n_(672356, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(672358)
    height_feet = height_feet
    _l_(672359)
    height_inches = _c_(672361, _n_(672360, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(672362)
    weight = _c_(672364, _n_(672363, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(672365)
    bmiout = _c_(672367, _n_(672366, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(672368)


    def calculate(self):
        _l_(672421)

        height_feet = _c_(672373, _n_(672369, "float", lambda: float), _a_(672372, _a_(672371, _n_(672370, "self", lambda: self), "height_feet"), "text"))
        _l_(672374)
        height_feet = _c_(672377, _n_(672375, "float", lambda: float), _n_(672376, "height_feet", lambda: height_feet) * 12)
        _l_(672378)
        height_inches = _c_(672383, _n_(672379, "float", lambda: float), _a_(672382, _a_(672381, _n_(672380, "self", lambda: self), "height_inches"), "text"))
        _l_(672384)
        height = _c_(672388, _n_(672385, "float", lambda: float), _n_(672386, "height_feet", lambda: height_feet) + _n_(672387, "height_inches", lambda: height_inches))
        _l_(672389)
        weight = _c_(672394, _n_(672390, "float", lambda: float), _a_(672393, _a_(672392, _n_(672391, "self", lambda: self), "weight"), "text"))
        _l_(672395)
        bmi = _c_(672400, _n_(672396, "int", lambda: int), _n_(672397, "weight", lambda: weight) / (_n_(672398, "height", lambda: height) * _n_(672399, "height", lambda: height)) * 703)
        _l_(672401)
        percent = _c_(672403, _n_(672402, "str", lambda: str), "%")
        _l_(672404)
        _a_(672406, _n_(672405, "self", lambda: self), "bmiout").text = _c_(672410, _a_(672407, "{}{}", "format"), _n_(672408, "bmi", lambda: bmi), _n_(672409, "percent", lambda: percent))
        _l_(672411)
        _a_(672413, _n_(672412, "self", lambda: self), "height_feet").text = ""
        _l_(672414)
        _a_(672416, _n_(672415, "self", lambda: self), "height_inches").text = ""
        _l_(672417)
        _a_(672419, _n_(672418, "self", lambda: self), "weight").text = ""
        _l_(672420)


    def __init__(self, **kwargs):
        _l_(672435)

        _n_(672422, "self", lambda: self).title = "BMI"
        _l_(672423)
        _a_(672425, _n_(672424, "self", lambda: self), "theme_cls").theme_style = "Dark"
        _l_(672426)
        _a_(672428, _n_(672427, "self", lambda: self), "theme_cls").primary_palette = "Blue"
        _l_(672429)
        _c_(672433, _a_(672431, _n_(672430, "super", lambda: super)(), "__init__"), **_n_(672432, "kwargs", lambda: kwargs))
        _l_(672434)



_c_(672440, _a_(672439, _c_(672438, _n_(672437, "MainApp", lambda: MainApp)), "run"))
_l_(672441)