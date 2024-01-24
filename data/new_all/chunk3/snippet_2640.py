# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68143331/scipy-optimise-typeerror-takes-1-positional-argument-but-2-were-given-with-ext
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(537944, _n_(537943, "njit", lambda: njit), cache=True)
def fn(x, weights):
    _l_(537951)

    aux = _c_(537949, _a_(537946, _n_(537945, "np", lambda: np), "sum"), (_n_(537947, "x", lambda: x) - _n_(537948, "weights", lambda: weights)) ** 2)
    _l_(537950)
    return aux


@_c_(537953, _n_(537952, "njit", lambda: njit), cache=True)
def fn_cons(x):
    _l_(537962)

    aux = _c_(537960, _a_(537955, _n_(537954, "np", lambda: np), "sum"), _c_(537959, _a_(537957, _n_(537956, "np", lambda: np), "abs"), _n_(537958, "x", lambda: x))) - 1
    _l_(537961)
    return aux


cons = ({'type': 'eq',
         'fun': _n_(537963, "fn_cons", lambda: fn_cons)
         })
_l_(537964)


class TestSpeedup:
    _l_(537993)


    def normalise(self, weights):
        _l_(537992)

        result = _c_(537978, _n_(537965, "minimize", lambda: minimize), _n_(537966, "fn", lambda: fn),
            _c_(537970, _a_(537968, _n_(537967, "np", lambda: np), "array"), _n_(537969, "weights", lambda: weights)),
            args=(_n_(537971, "weights", lambda: weights),),
            jac=lambda x: 2 * (_n_(537972, "x", lambda: x) - _n_(537973, "weights", lambda: weights)),
            bounds=[(0, _a_(537975, _n_(537974, "np", lambda: np), "infty")) for _ in _n_(537976, "weights", lambda: weights)],
            constraints=_n_(537977, "cons", lambda: cons)
        )
        _l_(537979)
        minimum = _a_(537981, _n_(537980, "result", lambda: result), "x")
        _l_(537982)
        aux = _n_(537983, "minimum", lambda: minimum) / _c_(537990, _a_(537985, _n_(537984, "np", lambda: np), "sum"), _c_(537989, _a_(537987, _n_(537986, "np", lambda: np), "abs"), _n_(537988, "minimum", lambda: minimum)))
        _l_(537991)

        # return np.max([new_weights, np.zeros(new_weights.size)], axis=0) / np.sum(np.max([new_weights, np.zeros(new_weights.size)], axis=0))
        return aux

weights = _c_(537996, _a_(537995, _n_(537994, "np", lambda: np), "array"), [ 1.04632843e+00, -6.89001783e-02,  2.17089646e-01, -2.52113073e-01, 4.19467585e-03])
_l_(537997)


test = _c_(537999, _n_(537998, "TestSpeedup", lambda: TestSpeedup))
_l_(538000)
result = _c_(538004, _a_(538002, _n_(538001, "test", lambda: test), "normalise"), _n_(538003, "weights", lambda: weights))
_l_(538005)