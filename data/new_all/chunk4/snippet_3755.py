# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68633532/error-plz-help-i-am-getting-attribute-error-even-when-i-have-specified-the-datat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def subsets(inp,out,index):
    _l_(582131)

    if _n_(582105, "index", lambda: index) >= _c_(582108, _n_(582106, "len", lambda: len), _n_(582107, "inp", lambda: inp)):
        _l_(582114)

        _c_(582111, _n_(582109, "print", lambda: print), _n_(582110, "out", lambda: out))
        _l_(582112)
        aux = "" 
        _l_(582113) 
        return aux 
    _c_(582119, _n_(582115, "subsets", lambda: subsets), _n_(582116, "inp", lambda: inp),_n_(582117, "out", lambda: out),_n_(582118, "index", lambda: index)+1)
    _l_(582120)
    _c_(582129, _n_(582121, "subsets", lambda: subsets), _n_(582122, "inp", lambda: inp),_c_(582127, _a_(582124, _n_(582123, "out", lambda: out), "append"), _n_(582125, "inp", lambda: inp)[_n_(582126, "index", lambda: index)]), _n_(582128, "index", lambda: index) +1)
    _l_(582130)
_c_(582133, _n_(582132, "subsets", lambda: subsets), [1,2,3],[],0)
_l_(582134)