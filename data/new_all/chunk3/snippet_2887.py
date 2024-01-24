# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59698266/typeerror-cant-multiply-sequence-by-non-int-of-type-numpy-float64-multiply
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list = []
_l_(555297)

i = 1
_l_(555298)
for col in _a_(555300, _n_(555299, "df", lambda: df), "columns")[1:19]:
    _l_(555355)


    #calculations
    x = _a_(555311, _n_(555301, "df", lambda: df)[[_a_(555303, _n_(555302, "df", lambda: df), "columns")[_n_(555304, "i", lambda: i)], _a_(555306, _n_(555305, "df", lambda: df), "columns")[_n_(555307, "i", lambda: i)+1], _a_(555309, _n_(555308, "df", lambda: df), "columns")[_n_(555310, "i", lambda: i)+2]]], "values")
    _l_(555312)
    Q = _c_(555317, _a_(555314, _n_(555313, "np", lambda: np), "cov"), _a_(555316, _n_(555315, "x", lambda: x), "T"))
    _l_(555318)

    eval, evec = _c_(555323, _a_(555321, _a_(555320, _n_(555319, "np", lambda: np), "linalg"), "eig"), _n_(555322, "Q", lambda: Q))
    _l_(555324)

    w = _c_(555333, _a_(555326, _n_(555325, "np", lambda: np), "array"), [2*(_n_(555327, "evec", lambda: evec)[0,2]/_n_(555328, "evec", lambda: evec)[1,2]),2*(_n_(555329, "evec", lambda: evec)[1,2]/_n_(555330, "evec", lambda: evec)[1,2]),2*(_n_(555331, "evec", lambda: evec)[2,2]/_n_(555332, "evec", lambda: evec)[1,2])])
    _l_(555334)

    #create new columns in dataframe with applied weights
    _n_(555335, "df", lambda: df)['w1_PCA'] = _a_(555337, _n_(555336, "df", lambda: df), "columns")[_n_(555338, "i", lambda: i)] * _n_(555339, "w", lambda: w)[0]
    _l_(555340)
    _n_(555341, "df", lambda: df)['b_PCA'] = _a_(555343, _n_(555342, "df", lambda: df), "columns")[_n_(555344, "i", lambda: i)+1] * _n_(555345, "w", lambda: w)[1]
    _l_(555346)
    _n_(555347, "df", lambda: df)['w2_PCA'] = _a_(555349, _n_(555348, "df", lambda: df), "columns")[_n_(555350, "i", lambda: i)+2] * _n_(555351, "w", lambda: w)[2]
    _l_(555352)

    i = _n_(555353, "i", lambda: i) + 1
    _l_(555354)

_c_(555358, _n_(555356, "print", lambda: print), _n_(555357, "x", lambda: x))
_l_(555359)