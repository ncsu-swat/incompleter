# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54991008/attributeerror-series-object-has-no-attribute-iterrows
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
accounts = _c_(405957, _a_(405955, _n_(405954, "pd", lambda: pd), "read_csv"), 'C:/*******/New_export.txt', sep=",", dtype={'number': _n_(405956, "object", lambda: object)})
_l_(405958)
_n_(405959, "accounts", lambda: accounts).columns = ["Number", "F"]
_l_(405960)

for i, j in _c_(405963, _a_(405962, _n_(405961, "accounts", lambda: accounts)["Number"], "iterrows")):
    _l_(405975)

    if (_c_(405966, _n_(405964, "str", lambda: str), _n_(405965, "j", lambda: j)) == "27*******5"):
        _l_(405974)

        _c_(405972, _n_(405967, "print", lambda: print), _n_(405968, "accounts", lambda: accounts)["F"][_n_(405969, "i", lambda: i)], _n_(405970, "accounts", lambda: accounts)["Number"][_n_(405971, "i", lambda: i)])
        _l_(405973)