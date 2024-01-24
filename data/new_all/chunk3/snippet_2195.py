# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58314475/django-typeerror-listserializer-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class KeyboardEventView(_a_(579012, _n_(579011, "viewsets", lambda: viewsets), "ModelViewSet")):
    _l_(579038)

    queryset = _c_(579015, _a_(579014, _a_(579013, KeyboardEvent, "objects"), "all"))
    _l_(579016)
    serializer_class = KeyboardEventSerializer
    _l_(579017)

    def get_serializer(self, *args, **kwargs):
        _l_(579037)

        if "data" in _n_(579018, "kwargs", lambda: kwargs):
            _l_(579028)

            data = _n_(579019, "kwargs", lambda: kwargs)["data"]
            _l_(579020)

            # check if many is required
            if _c_(579024, _n_(579021, "isinstance", lambda: isinstance), _n_(579022, "data", lambda: data), _n_(579023, "list", lambda: list)):
                _l_(579027)

                _n_(579025, "kwargs", lambda: kwargs)["many"] = True
                _l_(579026)
        aux = _c_(579035, _a_(579032, _n_(579029, "super", lambda: super)(_n_(579030, "KeyboardEventView", lambda: KeyboardEventView), _n_(579031, "self", lambda: self)), "get_serializer"), *_n_(579033, "args", lambda: args), **_n_(579034, "kwargs", lambda: kwargs))
        _l_(579036)

        return aux