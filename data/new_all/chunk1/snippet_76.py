# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60140174/basic-flask-app-not-running-typeerror-required-field-type-ignores-missing-fr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request, jsonify, abort, url_for
    _l_(415424)

except ImportError:
    pass

app = _c_(415427, _n_(415425, "Flask", lambda: Flask), _n_(415426, "__name__", lambda: __name__))
_l_(415428)

@_c_(415431, _a_(415430, _n_(415429, "app", lambda: app), "route"), '/')
def index():
    _l_(415435)

    aux = _c_(415433, _n_(415432, "jsonify", lambda: jsonify), {
        'success': True,
        'index': 'Test Pass'
    })
    _l_(415434)
    return aux



if _n_(415436, "__name__", lambda: __name__) == '__main__':
    _l_(415441)

    _c_(415439, _a_(415438, _n_(415437, "app", lambda: app), "run"), debug=True)
    _l_(415440)