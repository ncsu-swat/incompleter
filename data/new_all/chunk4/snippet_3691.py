# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69716472/how-do-i-solve-the-attribute-error-in-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.uix.widget import Widget
    _l_(632633)

except ImportError:
    pass
class widget_example(_n_(632634, "GridLayout", lambda: GridLayout)):
    _l_(632639)

    def button_click(self):
        _l_(632638)

        _c_(632636, _n_(632635, "print", lambda: print), 'button clicked')  
        _l_(632637)  
class MainWidget(_n_(632640, "Widget", lambda: Widget)):
    _l_(632642)

    pass
    _l_(632641)
class thelabapp(_n_(632643, "App", lambda: App)):
    _l_(632645)

    pass
    _l_(632644)

if _n_(632646, "__name__", lambda: __name__) == '__main__':
    _l_(632652)

    _c_(632650, _a_(632649, _c_(632648, _n_(632647, "thelabapp", lambda: thelabapp)), "run"))
    _l_(632651)