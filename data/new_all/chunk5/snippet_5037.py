# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33987368/custom-float-entry-for-tkinter-throwing-attribute-error-upon-deleting-contents
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FloatEntry(_a_(692329, _n_(692328, "tk", lambda: tk), "Entry")):
    _l_(692420)


    def __init__(self, master, default=0.0, **kwargs):
        _l_(692370)


        _c_(692336, _a_(692332, _a_(692331, _n_(692330, "tk", lambda: tk), "Entry"), "__init__"), _n_(692333, "self", lambda: self), _n_(692334, "master", lambda: master), **_n_(692335, "kwargs", lambda: kwargs))
        _l_(692337)
        _n_(692338, "self", lambda: self).default = _n_(692339, "default", lambda: default)
        _l_(692340)
        _n_(692341, "self", lambda: self).value = _a_(692343, _n_(692342, "self", lambda: self), "default")
        _l_(692344)
        _n_(692345, "self", lambda: self).float = _c_(692348, _a_(692347, _n_(692346, "tk", lambda: tk), "DoubleVar"))
        _l_(692349)
        _c_(692355, _a_(692352, _a_(692351, _n_(692350, "self", lambda: self), "float"), "set"), _a_(692354, _n_(692353, "self", lambda: self), "value"))
        _l_(692356)
        _c_(692362, _a_(692359, _a_(692358, _n_(692357, "self", lambda: self), "float"), "trace"), "w", _a_(692361, _n_(692360, "self", lambda: self), "__callback"))
        _l_(692363)
        _c_(692368, _a_(692365, _n_(692364, "self", lambda: self), "config"), textvariable=_a_(692367, _n_(692366, "self", lambda: self), "float"))
        _l_(692369)

    def __callback(self, *dummy):
        _l_(692406)

        value = _c_(692374, _a_(692373, _a_(692372, _n_(692371, "self", lambda: self), "float"), "get"))
        _l_(692375)
        new_value = _c_(692379, _a_(692377, _n_(692376, "self", lambda: self), "validate"), _n_(692378, "value", lambda: value))
        _l_(692380)
        if _n_(692381, "new_value", lambda: new_value) is None:
            _l_(692405)

            _c_(692387, _a_(692384, _a_(692383, _n_(692382, "self", lambda: self), "float"), "set"), _a_(692386, _n_(692385, "self", lambda: self), "default"))
            _l_(692388)
        elif _n_(692389, "new_value", lambda: new_value) != _n_(692390, "value", lambda: value):
            _l_(692404)

            _n_(692391, "self", lambda: self).value = _n_(692392, "new_value", lambda: new_value)
            _l_(692393)
            _c_(692399, _a_(692396, _a_(692395, _n_(692394, "self", lambda: self), "float"), "set"), _a_(692398, _n_(692397, "self", lambda: self), "new_value"))
            _l_(692400)
        else:
            _n_(692401, "self", lambda: self).value = _n_(692402, "value", lambda: value)
            _l_(692403)

    def validate(self, value):
        _l_(692419)

        try:
            _l_(692418)

            if _n_(692407, "value", lambda: value):
                _l_(692412)

                value = _c_(692410, _n_(692408, "float", lambda: float), _n_(692409, "value", lambda: value))
                _l_(692411)
            aux = _n_(692413, "value", lambda: value)
            _l_(692414)
            return aux
        except _n_(692415, "ValueError", lambda: ValueError):
            _l_(692417)

            aux = None
            _l_(692416)
            return aux