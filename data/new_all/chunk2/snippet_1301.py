# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51814886/del-tuple-keys-from-nested-dict-avoid-runtime-and-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for key, value in _c_(454698, _a_(454697, _n_(454696, "d_nans", lambda: d_nans), "items")):
    _l_(454716)

    seq_id = _n_(454699, "key", lambda: key)
    _l_(454700)
    feature_type = _n_(454701, "value", lambda: value)
    _l_(454702)
    for key, value in _c_(454705, _a_(454704, _n_(454703, "feature_type", lambda: feature_type), "items")):
        _l_(454715)

        for sub_key in _c_(454710, _n_(454706, "list", lambda: list), _c_(454709, _a_(454708, _n_(454707, "feature_type", lambda: feature_type), "keys"))):
            _l_(454714)

            if _n_(454711, "sub_key", lambda: sub_key)[0] == 'nan':
                _l_(454713)

                del dict[sub_key]
                _l_(454712)