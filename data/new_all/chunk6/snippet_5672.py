# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68551441/how-do-i-fix-attributeerror-list-object-has-no-attribute-strip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fin = _c_(374768, _n_(374767, "open", lambda: open), 'gift1.in','r')
_l_(374769)
p= _c_(374774, _a_(374773, _c_(374772, _a_(374771, _n_(374770, "fin", lambda: fin), "readline")), "split"), ",")
_l_(374775)
np = _c_(374780, _n_(374776, "int", lambda: int), _c_(374779, _a_(374778, _n_(374777, "p", lambda: p), "strip")))
_l_(374781)
dictOfMoney = { _c_(374786, _a_(374785, _c_(374784, _a_(374783, _n_(374782, "fin", lambda: fin), "readline")), "strip")) : 0 for i in _c_(374789, _n_(374787, "range", lambda: range), _n_(374788, "np", lambda: np)) }
_l_(374790)

while(True):
    _l_(374839)

    giver = _c_(374795, _a_(374794, _c_(374793, _a_(374792, _n_(374791, "fin", lambda: fin), "readline")), "strip"))
    _l_(374796)
    if(_n_(374797, "giver", lambda: giver)==""):
        _l_(374799)

        break
        _l_(374798)
    amount, divided = _c_(374809, _n_(374800, "map", lambda: map), _n_(374801, "int", lambda: int), _c_(374808, _a_(374807, _c_(374806, _a_(374805, _c_(374804, _a_(374803, _n_(374802, "fin", lambda: fin), "readline")), "strip")), "split")))
    _l_(374810)
    receivers = [_c_(374815, _a_(374814, _c_(374813, _a_(374812, _n_(374811, "fin", lambda: fin), "readline")), "strip")) for i in _c_(374818, _n_(374816, "range", lambda: range), _n_(374817, "divided", lambda: divided))]
    _l_(374819)

    try:
        _l_(374827)

        quotient, remainder = _c_(374823, _n_(374820, "divmod", lambda: divmod), _n_(374821, "amount", lambda: amount),_n_(374822, "divided", lambda: divided))
        _l_(374824)
    except:
        _l_(374826)

        quotient = remainder = 0
        _l_(374825)

    for receiver in _n_(374828, "receivers", lambda: receivers):
        _l_(374833)

        _n_(374829, "dictOfMoney", lambda: dictOfMoney)[_n_(374830, "receiver", lambda: receiver)] += _n_(374831, "quotient", lambda: quotient)
        _l_(374832)
    _n_(374834, "dictOfMoney", lambda: dictOfMoney)[_n_(374835, "giver", lambda: giver)] += -_n_(374836, "amount", lambda: amount) + _n_(374837, "remainder", lambda: remainder)
    _l_(374838)

with _c_(374841, _n_(374840, "open", lambda: open), 'gift1.out','w') as fout:
    _l_(374852)

    for name, money in _c_(374844, _a_(374843, _n_(374842, "dictOfMoney", lambda: dictOfMoney), "items")):
        _l_(374851)

        _c_(374849, _a_(374846, _n_(374845, "fout", lambda: fout), "write"), f"{_n_(374847, 'name', lambda: name)} {_n_(374848, 'money', lambda: money)}\n")
        _l_(374850)