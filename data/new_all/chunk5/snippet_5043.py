# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33987368/custom-float-entry-for-tkinter-throwing-attribute-error-upon-deleting-contents
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FloatEntry(_a_(683501, _n_(683500, "tk", lambda: tk), "Entry")):
    _l_(683592)


    def __init__(self, master, default=0.0, **kwargs):
        _l_(683542)


        _c_(683508, _a_(683504, _a_(683503, _n_(683502, "tk", lambda: tk), "Entry"), "__init__"), _n_(683505, "self", lambda: self), _n_(683506, "master", lambda: master), **_n_(683507, "kwargs", lambda: kwargs))
        _l_(683509)
        _n_(683510, "self", lambda: self).default = _n_(683511, "default", lambda: default)
        _l_(683512)
        _n_(683513, "self", lambda: self).value = _a_(683515, _n_(683514, "self", lambda: self), "default")
        _l_(683516)
        _n_(683517, "self", lambda: self).float = _c_(683520, _a_(683519, _n_(683518, "tk", lambda: tk), "DoubleVar"))
        _l_(683521)
        _c_(683527, _a_(683524, _a_(683523, _n_(683522, "self", lambda: self), "float"), "set"), _a_(683526, _n_(683525, "self", lambda: self), "value"))
        _l_(683528)
        _c_(683534, _a_(683531, _a_(683530, _n_(683529, "self", lambda: self), "float"), "trace"), "w", _a_(683533, _n_(683532, "self", lambda: self), "__callback"))
        _l_(683535)
        _c_(683540, _a_(683537, _n_(683536, "self", lambda: self), "config"), textvariable=_a_(683539, _n_(683538, "self", lambda: self), "float"))
        _l_(683541)

    def __callback(self, *dummy):
        _l_(683578)

        value = _c_(683546, _a_(683545, _a_(683544, _n_(683543, "self", lambda: self), "float"), "get"))
        _l_(683547)
        new_value = _c_(683551, _a_(683549, _n_(683548, "self", lambda: self), "validate"), _n_(683550, "value", lambda: value))
        _l_(683552)
        if _n_(683553, "new_value", lambda: new_value) is None:
            _l_(683577)

            _c_(683559, _a_(683556, _a_(683555, _n_(683554, "self", lambda: self), "float"), "set"), _a_(683558, _n_(683557, "self", lambda: self), "default"))
            _l_(683560)
        elif _n_(683561, "new_value", lambda: new_value) != _n_(683562, "value", lambda: value):
            _l_(683576)

            _n_(683563, "self", lambda: self).value = _n_(683564, "new_value", lambda: new_value)
            _l_(683565)
            _c_(683571, _a_(683568, _a_(683567, _n_(683566, "self", lambda: self), "float"), "set"), _a_(683570, _n_(683569, "self", lambda: self), "new_value"))
            _l_(683572)
        else:
            _n_(683573, "self", lambda: self).value = _n_(683574, "value", lambda: value)
            _l_(683575)

    def validate(self, value):
        _l_(683591)

        try:
            _l_(683590)

            if _n_(683579, "value", lambda: value):
                _l_(683584)

                value = _c_(683582, _n_(683580, "float", lambda: float), _n_(683581, "value", lambda: value))
                _l_(683583)
            aux = _n_(683585, "value", lambda: value)
            _l_(683586)
            return aux
        except _n_(683587, "ValueError", lambda: ValueError):
            _l_(683589)

            aux = None
            _l_(683588)
            return aux