# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51370082/nameerror-name-is-not-defined-passing-function-return-as-input-to-another
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(584409)

except ImportError:
    pass
def CreateDict(filename):
    _l_(584428)

    UsrDict = {}
    _l_(584410)
    with _c_(584413, _n_(584411, "open", lambda: open), _n_(584412, "filename", lambda: filename)) as csvfile:
        _l_(584427)

        readCSV = _c_(584417, _a_(584415, _n_(584414, "csv", lambda: csv), "reader"), _n_(584416, "csvfile", lambda: csvfile), delimiter=':')
        _l_(584418)
        for row in _n_(584419, "readCSV", lambda: readCSV):
            _l_(584424)

            _n_(584420, "UsrDict", lambda: UsrDict)[_n_(584421, "row", lambda: row)[0]]=_n_(584422, "row", lambda: row)[1]
            _l_(584423)
        aux = _n_(584425, "UsrDict", lambda: UsrDict)
        _l_(584426)
        return aux


def CreateHumanUsrNameDict(UsrDict):
    _l_(584446)

    HumanUsrDict={}
    _l_(584429)
    for k, v in _c_(584432, _a_(584431, _n_(584430, "HumanUsrDict", lambda: HumanUsrDict), "items")):
        _l_(584445)

        if _n_(584433, "v", lambda: v) == _c_(584435, _n_(584434, "len", lambda: len), 4):
            _l_(584440)

            _n_(584436, "HumanUsrDict", lambda: HumanUsrDict)[_n_(584437, "k", lambda: k):_n_(584438, "v", lambda: v)]
            _l_(584439)
        _c_(584443, _n_(584441, "print", lambda: print), _n_(584442, "HumanUsrDict", lambda: HumanUsrDict))
        _l_(584444)

if _n_(584447, "__name__", lambda: __name__)=='__main__':
    _l_(584455)

    _c_(584449, _n_(584448, "CreateDict", lambda: CreateDict), 'Book1.csv')
    _l_(584450)
    _c_(584453, _n_(584451, "CreateHumanUsrNameDict", lambda: CreateHumanUsrNameDict), _n_(584452, "UsrDict", lambda: UsrDict))
    _l_(584454)