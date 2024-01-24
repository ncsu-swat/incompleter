# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59362975/dont-understand-this-timed-while-loop-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(453720)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(453722)

except ImportError:
    pass
try:
    import time
    _l_(453724)

except ImportError:
    pass


test_num = 1
_l_(453725)
largest_loop = 0
_l_(453726)
delay = 60 * 10
_l_(453727)
end_time = _c_(453730, _a_(453729, _n_(453728, "time", lambda: time), "time")) + _n_(453731, "delay", lambda: delay)
_l_(453732)


def even_number(value):
    _l_(453736)

    if _n_(453733, "value", lambda: value) == 2:
        _l_(453735)

        aux = True
        _l_(453734)
        return aux


def divide_five(value):
    _l_(453740)

    if _n_(453737, "value", lambda: value) == 5:
        _l_(453739)

        aux = True
        _l_(453738)
        return aux


def is_square(value):
    _l_(453749)

    if _c_(453746, _a_(453745, _c_(453744, _a_(453742, _n_(453741, "math", lambda: math), "sqrt"), _n_(453743, "value", lambda: value)), "is_integer")):
        _l_(453748)

        aux = False
        _l_(453747)
        return aux


def multiple_of(value):
    _l_(453753)

    if _n_(453750, "value", lambda: value) == 2:
        _l_(453752)

        aux = True
        _l_(453751)
        return aux


def is_happy():
    _l_(453758)

    global check
    _l_(453754)
    if _n_(453755, "check", lambda: check) == 1:
        _l_(453757)

        aux = True
        _l_(453756)
        return aux


while _c_(453761, _a_(453760, _n_(453759, "time", lambda: time), "time")) <= _n_(453762, "end_time", lambda: end_time):
    _l_(453812)

    test_num += 1
    _l_(453763)
    check = _n_(453764, "test_num", lambda: test_num)
    _l_(453765)
    now = _c_(453768, _a_(453767, _n_(453766, "datetime", lambda: datetime), "now"))
    _l_(453769)
    loop_counter = 0
    _l_(453770)
    record_loop = 6
    _l_(453771)
    date = _c_(453774, _a_(453773, _n_(453772, "now", lambda: now), "strftime"), "%m/%d/%Y")
    _l_(453775)
    time = _c_(453778, _a_(453777, _n_(453776, "now", lambda: now), "strftime"), "%H:%M:%S")
    _l_(453779)
    if _c_(453782, _n_(453780, "even_number", lambda: even_number), _n_(453781, "test_num", lambda: test_num)) == True:
        _l_(453811)

        if _c_(453785, _n_(453783, "divide_five", lambda: divide_five), _n_(453784, "test_num", lambda: test_num)) == True:
            _l_(453809)

            if _c_(453788, _n_(453786, "is_square", lambda: is_square), _n_(453787, "test_num", lambda: test_num)) == True:
                _l_(453807)

                for _ in _c_(453791, _n_(453789, "range", lambda: range), _n_(453790, "record_loop", lambda: record_loop) + 4):
                    _l_(453805)

                    loop_counter += 1                            
                    _l_(453792)                            
                    if _c_(453794, _n_(453793, "is_happy", lambda: is_happy)) == True:
                        _l_(453803)

                        if _c_(453797, _n_(453795, "multiple_of", lambda: multiple_of), _n_(453796, "test_num", lambda: test_num)) == True:
                            _l_(453802)

                            #print(test_num)
                            record_loop = _n_(453798, "loop_counter", lambda: loop_counter)
                            _l_(453799)
                            break
                            _l_(453800)
                        else:
                            pass
                            _l_(453801)
                else:
                    pass
                    _l_(453804)
            else:
                pass
                _l_(453806)
        else:
            pass        
            _l_(453808)        
    else:
        pass
        _l_(453810)