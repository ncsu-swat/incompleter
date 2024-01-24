# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50176436/type-error-unsupported-operand
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_dig_pow(a, b):
    _l_(670921)

    dict1 = {}
    _l_(670878)
    for k in _c_(670882, _n_(670879, "range", lambda: range), _n_(670880, "a", lambda: a),_n_(670881, "b", lambda: b)+1):
        _l_(670918)

        if _n_(670883, "k", lambda: k) < 10:
            _l_(670917)

            _n_(670884, "dict1", lambda: dict1)[_n_(670885, "k", lambda: k)] = _n_(670886, "k", lambda: k)**1
            _l_(670887)

        else:
            num_len = _c_(670894, _n_(670888, "int", lambda: int), _c_(670893, _n_(670889, "len", lambda: len), _c_(670892, _n_(670890, "str", lambda: str), _n_(670891, "k", lambda: k)))) + 1
            _l_(670895)

            def dig_pow(k):
                _l_(670912)

                nonlocal num_len
                _l_(670896)
                num_len -= 1
                _l_(670897)
                if _n_(670898, "k", lambda: k) < 10:
                    _l_(670911)

                    aux = _n_(670899, "k", lambda: k)
                    _l_(670900)
                    return aux
                else:
                    var = (_n_(670901, "k", lambda: k)%10)**_n_(670902, "num_len", lambda: num_len) + _c_(670905, _n_(670903, "dig_pow", lambda: dig_pow), _n_(670904, "k", lambda: k)//10)
                    _l_(670906)
                    _n_(670907, "dict1", lambda: dict1)[_n_(670908, "k", lambda: k)] = _n_(670909, "var", lambda: var)
                    _l_(670910)

            _c_(670915, _n_(670913, "dig_pow", lambda: dig_pow), _n_(670914, "k", lambda: k))
            _l_(670916)
    aux = _n_(670919, "dict1", lambda: dict1)
    _l_(670920)
    return aux
_c_(670925, _n_(670922, "print", lambda: print), _c_(670924, _n_(670923, "sum_dig_pow", lambda: sum_dig_pow), 98, 100))
_l_(670926)