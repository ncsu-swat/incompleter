# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74811176/range-function-argument-returning-typeerror-not-all-arguments-converted-during
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for number in _n_(611299, "my_list", lambda: my_list):
    _l_(611316)

    if _n_(611300, "number", lambda: number)%3 ==0 and _n_(611301, "number", lambda: number)%5 ==0:
        _l_(611315)

        _n_(611302, "my_list", lambda: my_list)[_n_(611303, "number", lambda: number)] = "FizzBuzz"
        _l_(611304)
    elif _n_(611305, "number", lambda: number)%3 == 0:
        _l_(611314)

        _n_(611306, "my_list", lambda: my_list)[_n_(611307, "number", lambda: number)] = "Fizz"
        _l_(611308)
    elif _n_(611309, "number", lambda: number)%5 == 0:
        _l_(611313)

        _n_(611310, "my_list", lambda: my_list)[_n_(611311, "number", lambda: number)] ="Buzz"
        _l_(611312)
_c_(611319, _n_(611317, "print", lambda: print), _n_(611318, "my_list", lambda: my_list))
_l_(611320)