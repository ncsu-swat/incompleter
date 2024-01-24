# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51918256/python-merge-sort-typeerror-at-runtime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
l=[_c_(541014, _n_(541012, "int", lambda: int), _n_(541013, "n", lambda: n)) for n in _c_(541018, _a_(541017, _c_(541016, _n_(541015, "input", lambda: input)), "split"))]
_l_(541019)

def merge_sort(l):
    _l_(541100)

    if _c_(541022, _n_(541020, "len", lambda: len), _n_(541021, "l", lambda: l))==1:
        _l_(541099)

        aux = _n_(541023, "l", lambda: l)
        _l_(541024)
        return aux
    else:
        a=_n_(541025, "l", lambda: l)[:_c_(541028, _n_(541026, "len", lambda: len), _n_(541027, "l", lambda: l))//2]
        _l_(541029)
        b=_n_(541030, "l", lambda: l)[_c_(541033, _n_(541031, "len", lambda: len), _n_(541032, "l", lambda: l))//2:]
        _l_(541034)
        _c_(541038, _n_(541035, "print", lambda: print), _n_(541036, "a", lambda: a),_n_(541037, "b", lambda: b))
        _l_(541039)
        a=_c_(541042, _n_(541040, "merge_sort", lambda: merge_sort), _n_(541041, "a", lambda: a))
        _l_(541043)
        b=_c_(541046, _n_(541044, "merge_sort", lambda: merge_sort), _n_(541045, "b", lambda: b))
        _l_(541047)
        j=0
        _l_(541048)
        k=0
        _l_(541049)

        for i in _c_(541054, _n_(541050, "range", lambda: range), 0,_c_(541053, _n_(541051, "len", lambda: len), _n_(541052, "l", lambda: l))):
            _l_(541096)

            if  _n_(541055, "a", lambda: a)[_n_(541056, "j", lambda: j)] < _n_(541057, "b", lambda: b)[_n_(541058, "k", lambda: k)]:
                _l_(541095)

                _n_(541059, "l", lambda: l)[_n_(541060, "i", lambda: i)]=_n_(541061, "a", lambda: a)[_n_(541062, "j", lambda: j)]
                _l_(541063)
                j+=1
                _l_(541064)
                if _n_(541065, "j", lambda: j)==_c_(541068, _n_(541066, "len", lambda: len), _n_(541067, "a", lambda: a)):
                    _l_(541076)

                    l=_c_(541073, _a_(541070, _n_(541069, "l", lambda: l), "append"), _n_(541071, "b", lambda: b)[_n_(541072, "k", lambda: k):])
                    _l_(541074)
                    break
                    _l_(541075)
            else:
                _n_(541077, "l", lambda: l)[_n_(541078, "i", lambda: i)]=_n_(541079, "b", lambda: b)[_n_(541080, "k", lambda: k)]
                _l_(541081)
                k+=1
                _l_(541082)
                if _n_(541083, "k", lambda: k)==_c_(541086, _n_(541084, "len", lambda: len), _n_(541085, "b", lambda: b)):
                    _l_(541094)

                    l=_c_(541091, _a_(541088, _n_(541087, "l", lambda: l), "append"), _n_(541089, "a", lambda: a)[_n_(541090, "j", lambda: j):])
                    _l_(541092)
                    break
                    _l_(541093)
        aux = _n_(541097, "l", lambda: l)
        _l_(541098)
        # print(l)
        return aux

_c_(541105, _n_(541101, "print", lambda: print), _c_(541104, _n_(541102, "merge_sort", lambda: merge_sort), _n_(541103, "l", lambda: l)))
_l_(541106)