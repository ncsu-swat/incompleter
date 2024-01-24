# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43940194/kivy-typeerror-on-keyboard-down-takes-2-positional-arguments-but-5-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(449420, _a_(449419, _n_(449418, "Builder", lambda: Builder), "load_string"), '''
<PlayerImage>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            axis: (0, 0, 1)
            origin: self.center
    canvas.after:
        PopMatrix
<PlayerImage2>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            axis: (0, 0, 1)
            origin: self.center
    canvas.after:
        PopMatrix
''')
_l_(449421)