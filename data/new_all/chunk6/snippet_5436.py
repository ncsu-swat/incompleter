# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51370082/nameerror-name-is-not-defined-passing-function-return-as-input-to-another
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(341119)

except ImportError:
    pass
def CreateDict(filename):
    _l_(341138)

    UsrDict = {}
    _l_(341120)
    with _c_(341123, _n_(341121, "open", lambda: open), _n_(341122, "filename", lambda: filename)) as csvfile:
        _l_(341137)

        readCSV = _c_(341127, _a_(341125, _n_(341124, "csv", lambda: csv), "reader"), _n_(341126, "csvfile", lambda: csvfile), delimiter=':')
        _l_(341128)
        for row in _n_(341129, "readCSV", lambda: readCSV):
            _l_(341134)

            _n_(341130, "UsrDict", lambda: UsrDict)[_n_(341131, "row", lambda: row)[0]]=_n_(341132, "row", lambda: row)[1]
            _l_(341133)
        aux = _n_(341135, "UsrDict", lambda: UsrDict)
        _l_(341136)
        return aux


def CreateHumanUsrNameDict(UsrDict):
    _l_(341156)

    HumanUsrDict={}
    _l_(341139)
    for k, v in _c_(341142, _a_(341141, _n_(341140, "HumanUsrDict", lambda: HumanUsrDict), "items")):
        _l_(341155)

        if _n_(341143, "v", lambda: v) == _c_(341145, _n_(341144, "len", lambda: len), 4):
            _l_(341150)

            _n_(341146, "HumanUsrDict", lambda: HumanUsrDict)[_n_(341147, "k", lambda: k):_n_(341148, "v", lambda: v)]
            _l_(341149)
        _c_(341153, _n_(341151, "print", lambda: print), _n_(341152, "HumanUsrDict", lambda: HumanUsrDict))
        _l_(341154)

if _n_(341157, "__name__", lambda: __name__)=='__main__':
    _l_(341165)

    _c_(341159, _n_(341158, "CreateDict", lambda: CreateDict), 'Book1.csv')
    _l_(341160)
    _c_(341163, _n_(341161, "CreateHumanUsrNameDict", lambda: CreateHumanUsrNameDict), _n_(341162, "UsrDict", lambda: UsrDict))
    _l_(341164)