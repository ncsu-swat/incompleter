# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59117601/getting-typeerror-not-all-arguments-converted-during-string-formatting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse(num):
    _l_(658399)

    r=0
    _l_(658390)
    while(_n_(658391, "num", lambda: num)!=0):
        _l_(658396)

        r=(_n_(658392, "r", lambda: r)*10)+(_n_(658393, "num", lambda: num)%10)
        _l_(658394)
        num //= 10
        _l_(658395)
    aux = _n_(658397, "r", lambda: r)
    _l_(658398)
    return aux

num=_c_(658401, _n_(658400, "input", lambda: input), "Enter a number: ")
_l_(658402)
n=_c_(658405, _n_(658403, "reverse", lambda: reverse), _n_(658404, "num", lambda: num))
_l_(658406)
numOdd=[]
_l_(658407)
numEven=[]
_l_(658408)
c=1
_l_(658409)
while(_n_(658410, "n", lambda: n)!=0):
    _l_(658425)

    if (_n_(658411, "c", lambda: c)%2==0):
        _l_(658422)

        _c_(658415, _a_(658413, _n_(658412, "numEven", lambda: numEven), "append"), _n_(658414, "n", lambda: n)%10)
        _l_(658416)
    else:
        _c_(658420, _a_(658418, _n_(658417, "numOdd", lambda: numOdd), "append"), _n_(658419, "n", lambda: n)%10)
        _l_(658421)
    n//= 10
    _l_(658423)
    c += 1
    _l_(658424)
sortedEven=True
_l_(658426)
sortedOdd=True
_l_(658427)
for i in _c_(658432, _n_(658428, "range", lambda: range), _c_(658431, _n_(658429, "len", lambda: len), _n_(658430, "numOdd", lambda: numOdd))-1):
    _l_(658439)

    if(_n_(658433, "numOdd", lambda: numOdd)[_n_(658434, "i", lambda: i)]>_n_(658435, "numOdd", lambda: numOdd)[_n_(658436, "i", lambda: i)+1]):
        _l_(658438)

        sortedOdd=False
        _l_(658437)
for i in _c_(658444, _n_(658440, "range", lambda: range), _c_(658443, _n_(658441, "len", lambda: len), _n_(658442, "numEven", lambda: numEven))-1):
    _l_(658451)

    if(_n_(658445, "numEven", lambda: numEven)[_n_(658446, "i", lambda: i)]<_n_(658447, "numEven", lambda: numEven)[_n_(658448, "i", lambda: i)+1]):
        _l_(658450)

        sortedEven=False
        _l_(658449)

if(_n_(658452, "sortedOdd", lambda: sortedOdd)==True and _n_(658453, "sortedEven", lambda: sortedEven)==True):
    _l_(658460)

    _c_(658455, _n_(658454, "print", lambda: print), "True")
    _l_(658456)
else:
    _c_(658458, _n_(658457, "print", lambda: print), "False")
    _l_(658459)