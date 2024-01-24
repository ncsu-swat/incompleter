# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51028390/bottlepy-returning-typeerror-unhashable-type-set-with-if-clause
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bottle import route, template, request, post, run
    _l_(573821)

except ImportError:
    pass

@_c_(573823, _n_(573822, "route", lambda: route), '/')
def test_1():
    _l_(573827)

    aux = _c_(573825, _n_(573824, "template", lambda: template), 'test.html',
                    selected="F")
    _l_(573826)

    return aux

@_c_(573829, _n_(573828, "post", lambda: post), '/')
def response():
    _l_(573831)

    pass
    _l_(573830)

_c_(573833, _n_(573832, "run", lambda: run), host='localhost', port=8409)
_l_(573834)