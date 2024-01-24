# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74811176/range-function-argument-returning-typeerror-not-all-arguments-converted-during
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for number in _n_(586671, "my_list", lambda: my_list):
    _l_(586688)

    if _n_(586672, "number", lambda: number)%3 ==0 and _n_(586673, "number", lambda: number)%5 ==0:
        _l_(586687)

        _n_(586674, "my_list", lambda: my_list)[_n_(586675, "number", lambda: number)] = "FizzBuzz"
        _l_(586676)
    elif _n_(586677, "number", lambda: number)%3 == 0:
        _l_(586686)

        _n_(586678, "my_list", lambda: my_list)[_n_(586679, "number", lambda: number)] = "Fizz"
        _l_(586680)
    elif _n_(586681, "number", lambda: number)%5 == 0:
        _l_(586685)

        _n_(586682, "my_list", lambda: my_list)[_n_(586683, "number", lambda: number)] ="Buzz"
        _l_(586684)