# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67949407/typeerror-when-using-colorproperty-for-animation
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.lang import Builder
    _l_(596867)

except ImportError:
    pass
try:
    from kivy.animation import Animation
    _l_(596869)

except ImportError:
    pass
try:
    from kivy.properties import ColorProperty
    _l_(596871)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(596873)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(596875)

except ImportError:
    pass


class Custom(_n_(596876, "Button", lambda: Button)):
    _l_(596886)

    
    def change_color(self):
        _l_(596885)

        _c_(596883, _a_(596881, _c_(596880, _n_(596877, "Animation", lambda: Animation), background_color=_a_(596879, _n_(596878, "Example", lambda: Example), "fill_color")), "start"), _n_(596882, "self", lambda: self))
        _l_(596884)

class Example(_n_(596887, "App", lambda: App)):
    _l_(596906)

    fill_color = _c_(596889, _n_(596888, "ColorProperty", lambda: ColorProperty), [1, 0, 0, 1])
    _l_(596890)

    def __init__(self, **kwargs):
        _l_(596901)

        _c_(596894, _a_(596892, _n_(596891, "super", lambda: super)(), "__init__"), **_n_(596893, "kwargs", lambda: kwargs))
        _l_(596895)
        _n_(596896, "self", lambda: self).kv = _c_(596899, _a_(596898, _n_(596897, "Builder", lambda: Builder), "load_string"), '''
<Custom>:
    background_normal: ""
    background_color: 0, 0, 1, 1
    on_release: root.change_color()
Custom:
    text: "Turn me into Red!!"
    font_size: 32
''')
        _l_(596900)

    def build(self):
        _l_(596905)

        aux = _a_(596903, _n_(596902, "self", lambda: self), "kv")
        _l_(596904)
        return aux


if _n_(596907, "__name__", lambda: __name__) == "__main__":
    _l_(596913)

    _c_(596911, _a_(596910, _c_(596909, _n_(596908, "Example", lambda: Example)), "run"))
    _l_(596912)