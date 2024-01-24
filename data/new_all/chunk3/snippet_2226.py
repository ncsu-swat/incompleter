# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56798183/how-to-fix-attribute-error-when-using-pandas-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(532841, _n_(532840, "open", lambda: open), 'The Project- 6-21 E on leg arc test 1.csv', "r") as csvfile:
    _l_(532858)


    colnames = [ 'sensor', 'x', 'y', 'z', 'azimuth', 'elevation', 'roll', 'timestamp']
    _l_(532842)

    data = _c_(532846, _a_(532844, _n_(532843, "pd", lambda: pd), "read_csv"), 'The Project- 6-21 E on leg arc test 1.csv', names = _n_(532845, "colnames", lambda: colnames))
    _l_(532847)

    names = _c_(532851, _a_(532850, _a_(532849, _n_(532848, "data", lambda: data), "name"), "tolist"))
    _l_(532852)

    x = _c_(532856, _a_(532855, _a_(532854, _n_(532853, "data", lambda: data), "x"), "tolist"))
    _l_(532857)