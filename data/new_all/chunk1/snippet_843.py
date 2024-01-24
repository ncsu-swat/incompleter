# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63796878/typeerror-unknown-type-gstfraction
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gi
    _l_(400164)

except ImportError:
    pass

_c_(400167, _a_(400166, _n_(400165, "gi", lambda: gi), "require_version"), 'Gst', '1.0')
_l_(400168)
try:
    from gi.repository import Gst
    _l_(400170)

except ImportError:
    pass

_c_(400173, _a_(400172, _n_(400171, "Gst", lambda: Gst), "init"), None)
_l_(400174)

caps = _c_(400178, _a_(400177, _a_(400176, _n_(400175, "Gst", lambda: Gst), "Caps"), "from_string"), 'video/x-h264,width=640,height=480,framerate={30/1, 20/1, 15/1, 1/1}')
_l_(400179)
structure = _c_(400182, _a_(400181, _n_(400180, "caps", lambda: caps), "get_structure"), 0)
_l_(400183)

width = _a_(400187, _c_(400186, _a_(400185, _n_(400184, "structure", lambda: structure), "get_int"), 'width'), "value")
_l_(400188)
height = _a_(400192, _c_(400191, _a_(400190, _n_(400189, "structure", lambda: structure), "get_int"), 'height'), "value")
_l_(400193)
framerates = _a_(400197, _c_(400196, _a_(400195, _n_(400194, "structure", lambda: structure), "get_list"), 'framerate'), "array")
_l_(400198)

_c_(400201, _n_(400199, "print", lambda: print), 'width = ', _n_(400200, "width", lambda: width))
_l_(400202)
_c_(400205, _n_(400203, "print", lambda: print), 'height = ', _n_(400204, "height", lambda: height))
_l_(400206)
for i in _c_(400210, _n_(400207, "range", lambda: range), _a_(400209, _n_(400208, "framerates", lambda: framerates), "n_values")):
    _l_(400218)

    _c_(400216, _n_(400211, "print", lambda: print), ' - framerate = ', _c_(400215, _a_(400213, _n_(400212, "framerates", lambda: framerates), "get_nth"), _n_(400214, "i", lambda: i)))
    _l_(400217)