# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42600875/python-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def parallelUpdateJSON(submatrix):
    _l_(666243)

    with _c_(666214, _n_(666213, "open", lambda: open), 'geo.geojson') as f:
        _l_(666220)

        data = _c_(666218, _a_(666216, _n_(666215, "json", lambda: json), "load"), _n_(666217, "f", lambda: f))
        _l_(666219)
    for feature in _n_(666221, "data", lambda: data):
        _l_(666242)

        currentfeature = _n_(666222, "submatrix", lambda: submatrix)[(_n_(666223, "submatrix", lambda: submatrix)['SId']==_n_(666224, "feature", lambda: feature)['properties']['cellId'])]
        _l_(666225)
        if (_c_(666228, _n_(666226, "len", lambda: len), _n_(666227, "currentfeature", lambda: currentfeature)) > 0):
            _l_(666241)

            _c_(666235, _a_(666230, _n_(666229, "feature", lambda: feature)['properties'], "update"), {"style": {"opacity": _c_(666234, _a_(666233, _a_(666232, _n_(666231, "currentfeature", lambda: currentfeature), "AllActivity"), "item"))}})
            _l_(666236)
        else:
            _c_(666239, _a_(666238, _n_(666237, "feature", lambda: feature)['properties'], "update"), {"style": {"opacity": 0}})
            _l_(666240)


pool = _c_(666245, _n_(666244, "Pool", lambda: Pool))
_l_(666246)
_c_(666251, _a_(666248, _n_(666247, "pool", lambda: pool), "map"), _n_(666249, "parallelUpdateJSON", lambda: parallelUpdateJSON), _n_(666250, "submatrix", lambda: submatrix))
_l_(666252)
_c_(666255, _a_(666254, _n_(666253, "pool", lambda: pool), "close"))
_l_(666256)
_c_(666259, _a_(666258, _n_(666257, "pool", lambda: pool), "join"))
_l_(666260)