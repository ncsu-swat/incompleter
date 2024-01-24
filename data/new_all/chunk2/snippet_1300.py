# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51814886/del-tuple-keys-from-nested-dict-avoid-runtime-and-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for key, value in _c_(452610, _a_(452609, _n_(452608, "d_nans", lambda: d_nans), "items")):
    _l_(452627)

    seq_id = _n_(452611, "key", lambda: key)
    _l_(452612)
    feature_type = _n_(452613, "value", lambda: value)
    _l_(452614)
    for key, value in _c_(452617, _a_(452616, _n_(452615, "feature_type", lambda: feature_type), "items")):
        _l_(452626)

        if _c_(452620, _n_(452618, "type", lambda: type), _n_(452619, "key", lambda: key)) == _n_(452621, "tuple", lambda: tuple):
            _l_(452625)

            if _n_(452622, "key", lambda: key)[0] == 'nan':
                _l_(452624)

                del feature_type[key]
                _l_(452623)