# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66970261/attributeerror-str-object-has-no-attribute-configure
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(414331)

except ImportError:
    pass

root = _c_(414333, _n_(414332, "Tk", lambda: Tk))
_l_(414334)
_c_(414337, _a_(414336, _n_(414335, "root", lambda: root), "resizable"), width=False, height=False)
_l_(414338)

b1 = _c_(414343, _n_(414339, "Button", lambda: Button), _n_(414340, "root", lambda: root), text = '', width = 10, height = 5, command = lambda: _c_(414342, _n_(414341, "main", lambda: main), 1))
_l_(414344)
_c_(414347, _a_(414346, _n_(414345, "b1", lambda: b1), "grid"), row = 0, column = 1)
_l_(414348)
b2 = _c_(414353, _n_(414349, "Button", lambda: Button), _n_(414350, "root", lambda: root), text = '', width = 10, height = 5, command = lambda: _c_(414352, _n_(414351, "main", lambda: main), 2))
_l_(414354)
_c_(414357, _a_(414356, _n_(414355, "b2", lambda: b2), "grid"), row = 0, column = 2)
_l_(414358)
b3 = _c_(414363, _n_(414359, "Button", lambda: Button), _n_(414360, "root", lambda: root), text = '', width = 10, height = 5, command = lambda: _c_(414362, _n_(414361, "main", lambda: main), 3))
_l_(414364)
_c_(414367, _a_(414366, _n_(414365, "b3", lambda: b3), "grid"), row = 0, column = 3)
_l_(414368)
b4 = _c_(414373, _n_(414369, "Button", lambda: Button), _n_(414370, "root", lambda: root), text = '', width = 10, height = 5, command = lambda: _c_(414372, _n_(414371, "main", lambda: main), 4))
_l_(414374)
_c_(414377, _a_(414376, _n_(414375, "b4", lambda: b4), "grid"), row = 1, column = 1)
_l_(414378)
b5 = _c_(414383, _n_(414379, "Button", lambda: Button), _n_(414380, "root", lambda: root), text = '', width = 10, height = 5, command = lambda: _c_(414382, _n_(414381, "main", lambda: main), 5))
_l_(414384)
_c_(414387, _a_(414386, _n_(414385, "b5", lambda: b5), "grid"), row = 1, column = 2)
_l_(414388)
b6 = _c_(414393, _n_(414389, "Button", lambda: Button), _n_(414390, "root", lambda: root), text = '', width = 10, height = 5, command = lambda: _c_(414392, _n_(414391, "main", lambda: main), 6))
_l_(414394)
_c_(414397, _a_(414396, _n_(414395, "b6", lambda: b6), "grid"), row = 1, column = 3)
_l_(414398)

def main(num):
    _l_(414407)

    something = 'b' + _c_(414401, _n_(414399, "str", lambda: str), _n_(414400, "num", lambda: num))
    _l_(414402)
    _c_(414405, _a_(414404, _n_(414403, "something", lambda: something), "configure"), text = 'hi')
    _l_(414406)