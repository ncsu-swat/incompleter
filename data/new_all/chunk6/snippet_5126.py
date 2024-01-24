# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54547986/why-am-i-getting-nameerror-when-accessing-a-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ArmstrongNumber:
    _l_(364341)


    def cubesum(num):
        _l_(364324)

        aux = _c_(364322, _n_(364313, "sum", lambda: sum), [_c_(364316, _n_(364314, "int", lambda: int), _n_(364315, "i", lambda: i))**3 for i in _c_(364321, _n_(364317, "list", lambda: list), _c_(364320, _n_(364318, "str", lambda: str), _n_(364319, "num", lambda: num)))])
        _l_(364323)
        return aux

    def PrintArmstrong(num):
        _l_(364332)

        if _c_(364327, _n_(364325, "cubesum", lambda: cubesum), _n_(364326, "num", lambda: num)) == _n_(364328, "num", lambda: num):
            _l_(364330)

            aux = "Armstrong Number"
            _l_(364329)
            return aux
        aux = "Not an Armstrong Number"
        _l_(364331)
        return aux

    def Armstrong(num):
        _l_(364340)

        if _c_(364335, _n_(364333, "cubesum", lambda: cubesum), _n_(364334, "num", lambda: num)) == _n_(364336, "num", lambda: num):
            _l_(364338)

            aux = True
            _l_(364337)
            return aux
        aux = False
        _l_(364339)
        return aux

[_n_(364342, "i", lambda: i) for i in _c_(364344, _n_(364343, "range", lambda: range), 1000) if _c_(364348, _a_(364346, _n_(364345, "ArmstrongNumber", lambda: ArmstrongNumber), "Armstrong"), _n_(364347, "i", lambda: i))] # this return NameError
_l_(364349) # this return NameError