# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59117601/getting-typeerror-not-all-arguments-converted-during-string-formatting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse(num):
    _l_(656272)

    r=0
    _l_(656263)
    while(_n_(656264, "num", lambda: num)!=0):
        _l_(656269)

        r=(_n_(656265, "r", lambda: r)*10)+(_n_(656266, "num", lambda: num)%10)
        _l_(656267)
        num //= 10
        _l_(656268)
    aux = _n_(656270, "r", lambda: r)
    _l_(656271)
    return aux

num=_c_(656274, _n_(656273, "input", lambda: input), "Enter a number: ")
_l_(656275)
n=_c_(656278, _n_(656276, "reverse", lambda: reverse), _n_(656277, "num", lambda: num))
_l_(656279)
numOdd=[]
_l_(656280)
numEven=[]
_l_(656281)
c=1
_l_(656282)
while(_n_(656283, "n", lambda: n)!=0):
    _l_(656298)

    if (_n_(656284, "c", lambda: c)%2==0):
        _l_(656295)

        _c_(656288, _a_(656286, _n_(656285, "numEven", lambda: numEven), "append"), _n_(656287, "n", lambda: n)%10)
        _l_(656289)
    else:
        _c_(656293, _a_(656291, _n_(656290, "numOdd", lambda: numOdd), "append"), _n_(656292, "n", lambda: n)%10)
        _l_(656294)
    n//= 10
    _l_(656296)
    c += 1
    _l_(656297)
sortedEven=True
_l_(656299)
sortedOdd=True
_l_(656300)
for i in _c_(656305, _n_(656301, "range", lambda: range), _c_(656304, _n_(656302, "len", lambda: len), _n_(656303, "numOdd", lambda: numOdd))-1):
    _l_(656312)

    if(_n_(656306, "numOdd", lambda: numOdd)[_n_(656307, "i", lambda: i)]>_n_(656308, "numOdd", lambda: numOdd)[_n_(656309, "i", lambda: i)+1]):
        _l_(656311)

        sortedOdd=False
        _l_(656310)
for i in _c_(656317, _n_(656313, "range", lambda: range), _c_(656316, _n_(656314, "len", lambda: len), _n_(656315, "numEven", lambda: numEven))-1):
    _l_(656324)

    if(_n_(656318, "numEven", lambda: numEven)[_n_(656319, "i", lambda: i)]<_n_(656320, "numEven", lambda: numEven)[_n_(656321, "i", lambda: i)+1]):
        _l_(656323)

        sortedEven=False
        _l_(656322)

if(_n_(656325, "sortedOdd", lambda: sortedOdd)==True and _n_(656326, "sortedEven", lambda: sortedEven)==True):
    _l_(656333)

    _c_(656328, _n_(656327, "print", lambda: print), "True")
    _l_(656329)
else:
    _c_(656331, _n_(656330, "print", lambda: print), "False")
    _l_(656332)