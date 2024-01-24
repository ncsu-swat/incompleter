# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68151863/getting-typeerror-nonetype-object-is-not-subscriptable-on-api-when-runing-cod
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, jsonify, request
    _l_(593361)

except ImportError:
    pass
try:
    from flask_cors import CORS
    _l_(593363)

except ImportError:
    pass
try:
    from icecream import ic
    _l_(593365)

except ImportError:
    pass

app = _c_(593368, _n_(593366, "Flask", lambda: Flask), _n_(593367, "__name__", lambda: __name__))
_l_(593369)
_c_(593372, _n_(593370, "CORS", lambda: CORS), _n_(593371, "app", lambda: app))
_l_(593373)

@_c_(593376, _a_(593375, _n_(593374, "app", lambda: app), "route"), '/backend/signin', methods=['POST'])
def sign_in():
    _l_(593387)

    data = _a_(593378, _n_(593377, "request", lambda: request), "json")
    _l_(593379)
    _c_(593382, _n_(593380, "ic", lambda: ic), "*** app @ 53",_n_(593381, "data", lambda: data))
    _l_(593383)
    aux = {"username": _n_(593384, "data", lambda: data)['username'], "password":_n_(593385, "data", lambda: data)["password"]}
    _l_(593386)
    return aux

if _n_(593388, "__name__", lambda: __name__) == '__main__':
    _l_(593393)

    _c_(593391, _a_(593390, _n_(593389, "app", lambda: app), "run"), host='0.0.0.0', port=5050, debug=True)
    _l_(593392)