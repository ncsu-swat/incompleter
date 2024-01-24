# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70837963/name-error-in-class-when-importing-my-script-file-to-another-from
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(592005)

except ImportError:
    pass

class Operators:
    _l_(592041)


    def __init__(self, names):
        _l_(592016)

        
        _n_(592006, "self", lambda: self).op_name = []
        _l_(592007)

        for name in _n_(592008, "names", lambda: names):
            _l_(592015)

            _c_(592013, _a_(592011, _a_(592010, _n_(592009, "self", lambda: self), "op_name"), "append"), _n_(592012, "name", lambda: name))
            _l_(592014)
    
    def __matmul__(self, other):
        _l_(592031)


        if _c_(592019, _n_(592017, "type", lambda: type), _n_(592018, "other", lambda: other)) is _n_(592020, "Operators", lambda: Operators):
            _l_(592030)

            
            new_op_list = _a_(592022, _n_(592021, "self", lambda: self), "op_name") + _a_(592024, _n_(592023, "other", lambda: other), "op_name")
            _l_(592025)
            aux = _c_(592028, _n_(592026, "Operators", lambda: Operators), _n_(592027, "new_op_list", lambda: new_op_list))
            _l_(592029)
            
            return aux

    def __str__(self):
        _l_(592040)

        aux = _c_(592038, _a_(592032, ' @ ', "join"), _c_(592037, _n_(592033, "map", lambda: map), _n_(592034, "str", lambda: str), _a_(592036, _n_(592035, "self", lambda: self), "op_name")))
        _l_(592039)

        return aux



class Single_Ket:
    _l_(592091)


    def __init__(self, label: _n_(592042, "tuple", lambda: tuple), coeff, operator = []):
        _l_(592052)


        _n_(592043, "self", lambda: self).label = _n_(592044, "label", lambda: label)
        _l_(592045)
        _n_(592046, "self", lambda: self).coeff = _n_(592047, "coeff", lambda: coeff)
        _l_(592048)
        _n_(592049, "self", lambda: self).operators = _n_(592050, "operator", lambda: operator)
        _l_(592051)
    
    
    def __str__(self):
        _l_(592090)

        
        Operator_Str = _c_(592063, _n_(592053, "str", lambda: str), _c_(592062, _n_(592054, "eval", lambda: eval), _c_(592061, _a_(592055, ' @ ', "join"), _c_(592060, _n_(592056, "map", lambda: map), _n_(592057, "str", lambda: str), _a_(592059, _n_(592058, "self", lambda: self), "operators")))) )
        _l_(592064)
    
        if _c_(592068, _n_(592065, "type", lambda: type), _a_(592067, _n_(592066, "self", lambda: self), "label")) is _n_(592069, "tuple", lambda: tuple):
            _l_(592089)

            aux = _c_(592081, _a_(592070, '{} * {} @ | {} >', "format"), _a_(592072, _n_(592071, "self", lambda: self), "coeff"), _n_(592073, "Operator_Str", lambda: Operator_Str), _c_(592080, _a_(592074, ', ', "join"), _c_(592079, _n_(592075, "map", lambda: map), _n_(592076, "str", lambda: str), _a_(592078, _n_(592077, "self", lambda: self), "label"))))
            _l_(592082)
            
            return aux
        
        else:
            aux = f'{_a_(592084, _n_(592083, "self", lambda: self), "coeff")} * {_n_(592085, "Operator_Str", lambda: Operator_Str)}.|{_a_(592087, _n_(592086, "self", lambda: self), "label")}>'
            _l_(592088)
            return aux



if _n_(592092, '__name__', lambda: __name__) == '__main__':
    _l_(592108)


    
    Jp = _c_(592094, _n_(592093, 'Operators', lambda: Operators), ['Jp'])
    _l_(592095)
    Jm = _c_(592097, _n_(592096, 'Operators', lambda: Operators), ['Jm'])
    _l_(592098)


    ket_1 = _c_(592102, _n_(592099, 'Single_Ket', lambda: Single_Ket), (1, 1), 1, [_n_(592100, 'Jp', lambda: Jp) @ _n_(592101, 'Jm', lambda: Jm)])
    _l_(592103)

    _c_(592106, _n_(592104, 'print', lambda: print), _n_(592105, 'ket_1', lambda: ket_1))
    _l_(592107)