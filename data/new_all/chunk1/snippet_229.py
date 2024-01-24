# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59012381/pytest-flask-application-attributeerror-module-src-api-has-no-attribute-test
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, jsonify
    _l_(405994)

except ImportError:
    pass


api = _c_(405997, _n_(405995, "Flask", lambda: Flask), _n_(405996, "__name__", lambda: __name__))
_l_(405998)


@_c_(406001, _a_(406000, _n_(405999, "api", lambda: api), "route"), '/')
def hello_world():
    _l_(406005)

    aux = _c_(406003, _n_(406002, "jsonify", lambda: jsonify), message="hello world")
    _l_(406004)
    return aux


if _n_(406006, "__name__", lambda: __name__) == '__main__':
    _l_(406011)

    _c_(406009, _a_(406008, _n_(406007, "api", lambda: api), "run"), debug=True)
    _l_(406010)