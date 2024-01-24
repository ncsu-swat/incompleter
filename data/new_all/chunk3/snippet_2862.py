# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60641448/flask-restful-typeerror-object-of-type-record-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_restful import Resource, Api, reqparse
    _l_(541350)

except ImportError:
    pass

class _Weather(_n_(541351, "Resource", lambda: Resource)):
    _l_(541356)

    #WEATHER
    def get(self):
        _l_(541355)

        aux = {'value': _a_(541353, _n_(541352, "Weather", lambda: Weather), "Record")}
        _l_(541354)
        #GET WEATHER
        return aux

_c_(541361, _a_(541359, _a_(541358, _n_(541357, "self", lambda: self), "Api"), "add_resource"), _n_(541360, "_Weather", lambda: _Weather), '/api/weather')
_l_(541362)