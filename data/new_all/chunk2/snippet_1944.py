# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76785114/getting-kivy-attribute-error-super-object-has-no-attribute-getattr-pyth
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(472740)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(472742)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(472744)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(472746)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(472748)

except ImportError:
    pass
try:
    from kivy.uix.image import Image
    _l_(472750)

except ImportError:
    pass
try:
    import random
    _l_(472752)

except ImportError:
    pass
try:
    import os
    _l_(472754)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(472756)

except ImportError:
    pass
try:
    import numpy as np
    _l_(472758)

except ImportError:
    pass
try:
    from kivy.properties import StringProperty
    _l_(472760)

except ImportError:
    pass
try:
    from kivy.uix.floatlayout import FloatLayout
    _l_(472762)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(472764)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(472766)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(472768)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(472770)

except ImportError:
    pass
imp = "x"
_l_(472771)
user_inp = "x"
_l_(472772)


class MyLayout(_n_(472773, "Widget", lambda: Widget)):
    _l_(472790)

    #THIS IS WHERE THE ERROR SEEMS TO OCCUR
    def correct(self):
        _l_(472781)


        _a_(472776, _a_(472775, _n_(472774, "self", lambda: self), "ids"), "text_label").text = "Correct"
        _l_(472777)
        aux = _c_(472779, _n_(472778, "RootLayout", lambda: RootLayout))
        _l_(472780)
        return aux
    def incorrect(self):
        _l_(472789)

        _a_(472784, _a_(472783, _n_(472782, "self", lambda: self), "ids"), "text_label").text = "Incorrect"
        _l_(472785)
        aux = _c_(472787, _n_(472786, "RootLayout", lambda: RootLayout))
        _l_(472788)
        return aux

class RootLayout(_n_(472791, "FloatLayout", lambda: FloatLayout)):
    _l_(472793)

    pass
    _l_(472792)

prior = _c_(472795, _n_(472794, "StringProperty", lambda: StringProperty))
_l_(472796)

class colorApp(_n_(472797, "App", lambda: App), _n_(472798, "FloatLayout", lambda: FloatLayout)):
    _l_(472877)


    flagfile = _c_(472800, _n_(472799, "StringProperty", lambda: StringProperty), "0")
    _l_(472801)
    
    path = "/Users/sam/Downloads/App/w320"
    _l_(472802)
    files = _c_(472805, _a_(472804, _n_(472803, "os", lambda: os), "listdir"), path)
    _l_(472806)
    #self.important = random.choice(files)
    important = "bt.png"
    _l_(472807)
    flagfile= path + "/" + important
    _l_(472808)
    
    other_answer = _c_(472810, _n_(472809, "StringProperty", lambda: StringProperty))
    _l_(472811)
  
    prior = _c_(472813, _n_(472812, "StringProperty", lambda: StringProperty))
    _l_(472814)
    def button_press(self):
        _l_(472872)

        #[Removed Code]
 
        _c_(472818, _n_(472815, "print", lambda: print), _a_(472817, _n_(472816, "self", lambda: self), "correct_answer"))
        _l_(472819)
        _n_(472820, "self", lambda: self).imp = _a_(472822, _n_(472821, "self", lambda: self), "correct_answer")
        _l_(472823)
        
        _n_(472824, "self", lambda: self).prior = _c_(472831, _a_(472830, _a_(472829, _a_(472828, _a_(472827, _a_(472826, _n_(472825, "self", lambda: self), "root"), "ids"), "user_input"), "text"), "lower"))
        _l_(472832)

        user_inp = _a_(472834, _n_(472833, "self", lambda: self), "prior")
        _l_(472835)

        #THIS IS WHERE I CALL THE FUNCTION <------
        if _n_(472836, "user_inp", lambda: user_inp) == _a_(472838, _n_(472837, "self", lambda: self), "imp"):
            _l_(472849)

            _c_(472842, _a_(472841, _c_(472840, _n_(472839, "MyLayout", lambda: MyLayout)), "correct"))
            _l_(472843)
        else:
            _c_(472847, _a_(472846, _c_(472845, _n_(472844, "MyLayout", lambda: MyLayout)), "incorrect"))
            _l_(472848)
        
        _c_(472853, _n_(472850, "print", lambda: print), _a_(472852, _n_(472851, "self", lambda: self), "prior"))
        _l_(472854)
        _c_(472858, _n_(472855, "print", lambda: print), _a_(472857, _n_(472856, "self", lambda: self), "imp"))
        _l_(472859)
        _c_(472863, _n_(472860, "print", lambda: print), _a_(472862, _n_(472861, "self", lambda: self), "important"))
        _l_(472864)
        _c_(472867, _n_(472865, "print", lambda: print), _n_(472866, "user_inp", lambda: user_inp))
        _l_(472868)
        aux = _c_(472870, _n_(472869, "RootLayout", lambda: RootLayout))
        _l_(472871)

        return aux

    def build(self):
        _l_(472876)

        aux = _c_(472874, _n_(472873, "RootLayout", lambda: RootLayout))
        _l_(472875)
        return aux
if _n_(472878, "__name__", lambda: __name__) == "__main__":
    _l_(472884)

    _c_(472882, _a_(472881, _c_(472880, _n_(472879, "colorApp", lambda: colorApp)), "run"))
    _l_(472883)