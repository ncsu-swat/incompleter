# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60700244/example-code-on-kivy-document-keeps-giving-out-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
texture = _c_(533918, _a_(533917, _n_(533916, "Texture", lambda: Texture), "create"), size=(64, 64))
_l_(533919)

size = 64 * 64 * 3
_l_(533920)
buf = [_c_(533924, _n_(533921, "int", lambda: int), _n_(533922, "x", lambda: x) * 255 / _n_(533923, "size", lambda: size)) for x in _c_(533927, _n_(533925, "range", lambda: range), _n_(533926, "size", lambda: size))]
_l_(533928)

buf = _c_(533934, _a_(533929, b'', "join"), _c_(533933, _n_(533930, "map", lambda: map), _n_(533931, "chr", lambda: chr), _n_(533932, "buf", lambda: buf)))    # This is the code with a problem
_l_(533935)    # This is the code with a problem

_c_(533939, _a_(533937, _n_(533936, "texture", lambda: texture), "blit_buffer"), _n_(533938, "buf", lambda: buf), colorfmt='rgb', bufferfmt='ubyte')
_l_(533940)
with _a_(533942, _n_(533941, "self", lambda: self), "canvas"):
    _l_(533949)

    _c_(533947, _n_(533943, "Rectangle", lambda: Rectangle), texture=_n_(533944, "texture", lambda: texture), pos=_a_(533946, _n_(533945, "self", lambda: self), "pos"), size=(64, 64))
    _l_(533948)