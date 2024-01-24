# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63009363/name-error-data-is-not-defined-when-sending-post-request-values-from-react-to-fl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        from flask import Flask, request, json
        _l_(530936)

except ImportError:
        pass


app = _c_(530939, _n_(530937, "Flask", lambda: Flask), _n_(530938, "__name__", lambda: __name__))
_l_(530940)

@_c_(530943, _a_(530942, _n_(530941, "app", lambda: app), "route"), '/api', methods=['GET','POST'])
def api():
        _l_(530947)

        data = _a_(530945, _n_(530944, "request", lambda: request), "form")['username']
        _l_(530946)
_c_(530950, _n_(530948, "print", lambda: print), _n_(530949, "data", lambda: data))
_l_(530951)