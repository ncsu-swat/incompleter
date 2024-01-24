# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42573566/python-decorator-typeerror-function-takes-1-positional-argument-but-2-were-giv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(388657, "log_calls", lambda: log_calls)
def fizz_buzz_or_number(i):
    _l_(388670)

    ''' Return "fizz" if i is divisible by 3, "buzz" if by
        5, and "fizzbuzz" if both; otherwise, return i. '''
    _l_(388658)
    if _n_(388659, "i", lambda: i) % 15 == 0:
        _l_(388669)

        aux = 'fizzbuzz'
        _l_(388660)
        return aux
    elif _n_(388661, "i", lambda: i) % 3 == 0:
        _l_(388668)

        aux = 'fizz'
        _l_(388662)
        return aux
    elif _n_(388663, "i", lambda: i) % 5 == 0:
        _l_(388667)

        aux = 'buzz'
        _l_(388664)
        return aux
    else:
        aux = _n_(388665, "i", lambda: i)
        _l_(388666)
        return aux