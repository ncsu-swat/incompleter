# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49964078/trying-to-implement-a-lisp-program-on-python-error-builtins-typeerror-int-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def s_sum(l):
    _l_(540911)


    if _n_(540894, "l", lambda: l) == []:
        _l_(540910)

        aux = 0
        _l_(540895)
        return aux
    else:
       _c_(540898, _n_(540896, "print", lambda: print), _n_(540897, "l", lambda: l)[:])
       _l_(540899)
       aux = _c_(540905, _a_(540901, _n_(540900, "l", lambda: l), "append"), _c_(540904, _n_(540902, "sum_numbers", lambda: sum_numbers), _n_(540903, "l", lambda: l)[0])) + _c_(540908, _n_(540906, "s_sum", lambda: s_sum), _n_(540907, "l", lambda: l)[1:])
       _l_(540909)
       # print(s_sum(l[1:]))
       return aux

def sum_numbers(l):
    _l_(540941)

    if _n_(540912, "l", lambda: l) == []:
        _l_(540940)

        aux = 0
        _l_(540913)
        return aux
    elif _c_(540916, _n_(540914, "type", lambda: type), _n_(540915, "l", lambda: l)[0]) is _n_(540917, "int", lambda: int):
        _l_(540939)

        aux = _n_(540918, "l", lambda: l)[0] + _c_(540921, _n_(540919, "sum_numbers", lambda: sum_numbers), _n_(540920, "l", lambda: l)[1:])
        _l_(540922)
        return aux
    elif _c_(540926, _n_(540923, "isinstance", lambda: isinstance), _n_(540924, "l", lambda: l)[0], _n_(540925, "str", lambda: str) ):
        _l_(540938)

        aux = _c_(540929, _n_(540927, "sum_numbers", lambda: sum_numbers), _n_(540928, "l", lambda: l)[1:])
        _l_(540930)
        return aux
    else:
        aux = _c_(540933, _n_(540931, "sum_numbers", lambda: sum_numbers), _n_(540932, "l", lambda: l)[0]) + _c_(540936, _n_(540934, "sum_numbers", lambda: sum_numbers), _n_(540935, "l", lambda: l)[1:])
        _l_(540937)
        return aux


#l = list(input().split())
l = [ [ 1, 'h', 1, 'e' ], [ 5, 'b', 9 ], [ 4, 'k'] ]
_l_(540942)
#print(l)
_c_(540945, _n_(540943, "s_sum", lambda: s_sum), _n_(540944, "l", lambda: l))
_l_(540946)