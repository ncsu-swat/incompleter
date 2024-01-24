# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56414829/attributeerror-module-rsvg-has-no-attribute-handle
#some code to give rsvg.render_cairo(ctx) ability
#on windows.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(677158)

except ImportError:
    pass
try:
    _l_(677257)

    import rsvg
    _l_(677159)
    WINDOWS=False
    _l_(677160)
except _n_(677161, "ImportError", lambda: ImportError):
    _l_(677256)

    _c_(677163, _n_(677162, "print", lambda: print), "Warning, could not import 'rsvg'")
    _l_(677164)
    if _a_(677166, _n_(677165, "os", lambda: os), "name") == 'nt':
        _l_(677255)

        _c_(677168, _n_(677167, "print", lambda: print), "Detected windows, creating rsvg.")
        _l_(677169)
        try:
            from ctypes import *
            _l_(677171)

        except ImportError:
            pass

        l=_c_(677173, _n_(677172, "CDLL", lambda: CDLL), 'librsvg-2-2.dll')
        _l_(677174)
        g=_c_(677176, _n_(677175, "CDLL", lambda: CDLL), 'libgobject-2.0-0.dll')
        _l_(677177)
        _c_(677180, _a_(677179, _n_(677178, "g", lambda: g), "g_type_init"))
        _l_(677181)

        class rsvgHandle():
            _l_(677245)

            class RsvgDimensionData(Structure):
                _l_(677183)

                _fields_ = [("width", c_int),
                            ("height", c_int),
                            ("em",c_double),
                            ("ex",c_double)]
                _l_(677182)

            class PycairoContext(Structure):
                _l_(677187)

                _fields_ = [("PyObject_HEAD", c_byte * _a_(677185, _n_(677184, "object", lambda: object), "__basicsize__")),
                            ("ctx", c_void_p),
                            ("base", c_void_p)]
                _l_(677186)

            def __init__(self, path):
                _l_(677200)

                _n_(677188, "self", lambda: self).path = _n_(677189, "path", lambda: path)
                _l_(677190)
                error = ''
                _l_(677191)
                _n_(677192, "self", lambda: self).handle = _c_(677198, _a_(677194, _n_(677193, "l", lambda: l), "rsvg_handle_new_from_file"), _a_(677196, _n_(677195, "self", lambda: self), "path"),_n_(677197, "error", lambda: error))
                _l_(677199)


            def get_dimension_data(self):
                _l_(677219)

                svgDim = _c_(677203, _a_(677202, _n_(677201, "self", lambda: self), "RsvgDimensionData"))
                _l_(677204)
                _c_(677212, _a_(677206, _n_(677205, "l", lambda: l), "rsvg_handle_get_dimensions"), _a_(677208, _n_(677207, "self", lambda: self), "handle"),_c_(677211, _n_(677209, "byref", lambda: byref), _n_(677210, "svgDim", lambda: svgDim)))
                _l_(677213)
                aux = (_a_(677215, _n_(677214, "svgDim", lambda: svgDim), "width"),_a_(677217, _n_(677216, "svgDim", lambda: svgDim), "height"))
                _l_(677218)
                return aux

            def render_cairo(self, ctx):
                _l_(677244)

                _c_(677222, _a_(677221, _n_(677220, "ctx", lambda: ctx), "save"))
                _l_(677223)
                z = _c_(677230, _a_(677226, _a_(677225, _n_(677224, "self", lambda: self), "PycairoContext"), "from_address"), _c_(677229, _n_(677227, "id", lambda: id), _n_(677228, "ctx", lambda: ctx)))
                _l_(677231)
                _c_(677238, _a_(677233, _n_(677232, "l", lambda: l), "rsvg_handle_render_cairo"), _a_(677235, _n_(677234, "self", lambda: self), "handle"), _a_(677237, _n_(677236, "z", lambda: z), "ctx"))
                _l_(677239)
                _c_(677242, _a_(677241, _n_(677240, "ctx", lambda: ctx), "restore"))
                _l_(677243)



        class rsvgClass():
            _l_(677251)

            def Handle(self,file):
                _l_(677250)

                aux = _c_(677248, _n_(677246, "rsvgHandle", lambda: rsvgHandle), _n_(677247, "file", lambda: file))
                _l_(677249)
                return aux

        rsvg = _c_(677253, _n_(677252, "rsvgClass", lambda: rsvgClass))
        _l_(677254)
h = _c_(677260, _a_(677259, _n_(677258, "rsvg", lambda: rsvg), "Handle"), "index.svg")
_l_(677261)
s = _c_(677266, _a_(677263, _n_(677262, "cairo", lambda: cairo), "ImageSurface"), _a_(677265, _n_(677264, "cairo", lambda: cairo), "FORMAT_ARGB32"), 100, 100)
_l_(677267)
ctx = _c_(677271, _a_(677269, _n_(677268, "cairo", lambda: cairo), "Context"), _n_(677270, "s", lambda: s))
_l_(677272)
_c_(677276, _a_(677274, _n_(677273, "h", lambda: h), "render_cairo"), _n_(677275, "ctx", lambda: ctx))
_l_(677277)