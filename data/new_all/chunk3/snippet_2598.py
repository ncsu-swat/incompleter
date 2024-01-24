# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70048468/python-filenotfounderror-even-if-the-file-is-there
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(572206)

except ImportError:
    pass
try:
    from pyglet import font
    _l_(572208)

except ImportError:
    pass
_c_(572216, _a_(572210, _n_(572209, "font", lambda: font), "add_file"), _c_(572215, _n_(572211, "str", lambda: str), _c_(572214, _a_(572213, _n_(572212, "os", lambda: os), "getcwd")))+"\\fonts\\Roboto Bold.ttf")
_l_(572217)