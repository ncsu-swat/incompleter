# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48104288/typeerror-initial-value-must-be-str-or-none-not-bytes
# -*- coding : utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(474488)

except ImportError:
    pass
try:
    import requests
    _l_(474490)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(474492)

except ImportError:
    pass
try:
    from io import StringIO
    _l_(474494)

except ImportError:
    pass


class Window:
    _l_(474575)

    def __init__(self, master):
        _l_(474545)

        _n_(474495, "self", lambda: self).master = _n_(474496, "master", lambda: master)
        _l_(474497)
        _n_(474498, "self", lambda: self).url = _c_(474501, _a_(474500, _n_(474499, "tk", lambda: tk), "Entry"))
        _l_(474502)
        _c_(474506, _a_(474505, _a_(474504, _n_(474503, "self", lambda: self), "url"), "get"))
        _l_(474507)
        _c_(474511, _a_(474510, _a_(474509, _n_(474508, "self", lambda: self), "url"), "grid"), row=0, column=1)
        _l_(474512)
        _n_(474513, "self", lambda: self).button = _c_(474518, _a_(474515, _n_(474514, "tk", lambda: tk), "Button"), text="Download", command=_a_(474517, _n_(474516, "self", lambda: self), "get_url"))
        _l_(474519)
        _c_(474523, _a_(474522, _a_(474521, _n_(474520, "self", lambda: self), "button"), "grid"), row=0, column=0)
        _l_(474524)
        _n_(474525, "self", lambda: self).label = _c_(474528, _a_(474527, _n_(474526, "tk", lambda: tk), "Label"), text="Name")
        _l_(474529)
        _c_(474533, _a_(474532, _a_(474531, _n_(474530, "self", lambda: self), "label"), "grid"), row=1, column=0)
        _l_(474534)
        _n_(474535, "self", lambda: self).path = _c_(474538, _a_(474537, _n_(474536, "tk", lambda: tk), "Entry"))
        _l_(474539)
        _c_(474543, _a_(474542, _a_(474541, _n_(474540, "self", lambda: self), "path"), "grid"), row=1, column=1)
        _l_(474544)

    def get_url(self):
        _l_(474574)

        _n_(474546, "self", lambda: self).r = _c_(474553, _a_(474548, _n_(474547, "requests", lambda: requests), "get"), _c_(474552, _a_(474551, _a_(474550, _n_(474549, "self", lambda: self), "url"), "get")))
        _l_(474554)
        _n_(474555, "self", lambda: self).i = _c_(474563, _a_(474557, _n_(474556, "Image", lambda: Image), "open"), _c_(474562, _n_(474558, "StringIO", lambda: StringIO), _a_(474561, _a_(474560, _n_(474559, "self", lambda: self), "r"), "content")))
        _l_(474564)
        _c_(474572, _a_(474567, _a_(474566, _n_(474565, "self", lambda: self), "i"), "save"), _c_(474571, _a_(474570, _a_(474569, _n_(474568, "self", lambda: self), "path"), "get")))
        _l_(474573)


def main():
    _l_(474588)

    root = _c_(474578, _a_(474577, _n_(474576, "tk", lambda: tk), "Tk"))
    _l_(474579)
    w = _c_(474582, _n_(474580, "Window", lambda: Window), _n_(474581, "root", lambda: root))
    _l_(474583)
    _c_(474586, _a_(474585, _n_(474584, "root", lambda: root), "mainloop"))
    _l_(474587)


if _n_(474589, "__name__", lambda: __name__) == "__main__":
    _l_(474593)

    _c_(474591, _n_(474590, "main", lambda: main))
    _l_(474592)