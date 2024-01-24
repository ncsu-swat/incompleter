# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52008881/flask-attributeerror-blueprint-object-has-no-attribute-response-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(455058, _a_(455057, _n_(455056, "bp", lambda: bp), "route"), '/output_stream', methods=['GET', 'POST'])
def output_stream():
    _l_(455101)

    def generate():
        _l_(455094)

        if _a_(455060, _n_(455059, "request", lambda: request), "method") == "POST":
            _l_(455093)

            ...
            _l_(455061)
            ...
            _l_(455062)
            for line in _c_(455067, _n_(455063, "iter", lambda: iter), lambda: _c_(455066, _a_(455065, _n_(455064, "stdout", lambda: stdout), "readline"), 2048), ""):
                _l_(455085)

                data_buffer += _n_(455068, "line", lambda: line)
                _l_(455069)
                _c_(455072, _n_(455070, "print", lambda: print), _n_(455071, "line", lambda: line), end="")
                _l_(455073)
                yield _n_(455074, "line", lambda: line) + '\n'
                _l_(455075)
                if _c_(455079, _a_(455077, _n_(455076, "re", lambda: re), "search"), r'Done', _n_(455078, "line", lambda: line)):
                    _l_(455084)

                    _c_(455081, _n_(455080, "print", lambda: print), 'No more data')
                    _l_(455082)
                    break
                    _l_(455083)

            _c_(455087, _n_(455086, "print", lambda: print), 'finished.')
            _l_(455088)

            _c_(455091, _a_(455090, _n_(455089, "client", lambda: client), "close"))
            _l_(455092)
    aux = _c_(455099, _a_(455096, _n_(455095, "bp", lambda: bp), "response_class"), _c_(455098, _n_(455097, "generate", lambda: generate)), mimetype='text/plain')
    _l_(455100)

    return aux