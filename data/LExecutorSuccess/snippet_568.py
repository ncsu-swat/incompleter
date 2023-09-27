# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/18265935/how-do-i-create-a-list-with-numbers-between-two-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
start=0
_l_(1542953)
end=10
_l_(1542954)
arr=_c_(1542960, _n_(1542955, "list", lambda: list), _c_(1542959, _n_(1542956, "range", lambda: range), _n_(1542957, "start", lambda: start),_n_(1542958, "end", lambda: end)+1))
_l_(1542961)
output: _n_(1542962, "arr", lambda: arr)=[0,1,2,3,4,5,6,7,8,9,10]
_l_(1542963)

ar=[]
_l_(1542964)
def diff(start,end):
    _l_(1542985)

    if _n_(1542965, "start", lambda: start)==_n_(1542966, "end", lambda: end):
        _l_(1542984)

        _c_(1542970, _a_(1542968, _n_(1542967, "d", lambda: d), "append"), _n_(1542969, "end", lambda: end))
        _l_(1542971)
        aux = _n_(1542972, "ar", lambda: ar)
        _l_(1542973)
        return aux
    else:
        _c_(1542977, _a_(1542975, _n_(1542974, "ar", lambda: ar), "append"), _n_(1542976, "end", lambda: end))
        _l_(1542978)
        aux = _c_(1542982, _n_(1542979, "diff", lambda: diff), _n_(1542980, "start", lambda: start)-1,_n_(1542981, "end", lambda: end)) 
        _l_(1542983) 
        return aux 

