# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74565149/global-variable-doesnt-work-how-do-i-get-the-same-exact-value-of-a-variable-ou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def validate_pnr(ips):
    _l_(581153)

    sum_odd = 0
    _l_(581112)
    sum_even = 0
    _l_(581113)
    total = 0 
    _l_(581114) 
    #global diva
    ips = _c_(581117, _a_(581116, _n_(581115, "ips", lambda: ips), "replace"), "-", "")
    _l_(581118)
    ips = _c_(581121, _a_(581120, _n_(581119, "ips", lambda: ips), "replace"), " ", "")
    _l_(581122)
    ips = _n_(581123, "ips", lambda: ips)[::-1]
    _l_(581124)
    
    for digit in _n_(581125, "ips", lambda: ips)[::2]:
        _l_(581130)

        sum_odd += _c_(581128, _n_(581126, "int", lambda: int), _n_(581127, "digit", lambda: digit))
        _l_(581129)

    for digit in _n_(581131, "ips", lambda: ips)[1::2]:
        _l_(581142)

        digit = _c_(581134, _n_(581132, "int", lambda: int), _n_(581133, "digit", lambda: digit)) * 2
        _l_(581135)
        if _n_(581136, "digit", lambda: digit) >= 10:
            _l_(581141)

            sum_even += (1+(_n_(581137, "digit", lambda: digit) % 10))
            _l_(581138)
        else:
            sum_even += _n_(581139, "digit", lambda: digit)
            _l_(581140)

    total = _n_(581143, "sum_odd", lambda: sum_odd) + _n_(581144, "sum_even", lambda: sum_even)
    _l_(581145)
    divide = _n_(581146, "total", lambda: total) % 10 == 0
    _l_(581147)
    diva = _n_(581148, "divide", lambda: divide)
    _l_(581149)
    aux = _n_(581150, "diva", lambda: diva) and _n_(581151, "ips", lambda: ips)
    _l_(581152)
 
    return aux


if _n_(581154, "__name__", lambda: __name__) == "__main__":
    _l_(581183)


    _c_(581156, _n_(581155, "print", lambda: print), "Welcome to National Provider Identifier numbers (NPI) validator")
    _l_(581157)
    _c_(581159, _n_(581158, "print", lambda: print), "Write in the format (YYMMDD-NNNN):")
    _l_(581160)
    answer= _c_(581162, _n_(581161, "input", lambda: input), "You want to try? (Y/N): ")
    _l_(581163)

    while _n_(581164, "answer", lambda: answer) != "N":
        _l_(581182)

        ips = _c_(581166, _n_(581165, "input", lambda: input), "Write in the format (YYMMDD-NNNN): ")
        _l_(581167)
        while _n_(581168, "diva", lambda: diva) == True:
            _l_(581181)

            _c_(581171, _n_(581169, "validate_pnr", lambda: validate_pnr), _n_(581170, "ips", lambda: ips))
            _l_(581172)
            answer = _c_(581174, _n_(581173, "input", lambda: input), "You want to try another one? (Y/N): ")
            _l_(581175)
            if _n_(581176, "answer", lambda: answer) == "N":
                _l_(581180)

                _c_(581178, _n_(581177, "print", lambda: print), "Program is executing...")
                _l_(581179)