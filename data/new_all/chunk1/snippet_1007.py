# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54598635/typeerror-unsupported-operand-types-for-int-and-list-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(400980)

    def maxSubArray(self,A):
        _l_(400979)

        sum_2=[]
        _l_(400946)

        for i in _c_(400951, _n_(400947, "range", lambda: range), 0,_c_(400950, _n_(400948, "len", lambda: len), _n_(400949, "A", lambda: A))):
            _l_(400968)

            for j in _c_(400956, _n_(400952, "range", lambda: range), 1,_c_(400955, _n_(400953, "len", lambda: len), _n_(400954, "A", lambda: A))-1):
                _l_(400967)



                sum_1 = _n_(400957, "A", lambda: A)[_n_(400958, "i", lambda: i)]+_n_(400959, "A", lambda: A)[:_n_(400960, "j", lambda: j)]
                _l_(400961)
                _c_(400965, _a_(400963, _n_(400962, "sum_2", lambda: sum_2), "append"), _n_(400964, "sum_1", lambda: sum_1))
                _l_(400966)
        _c_(400971, _n_(400969, "print", lambda: print), _n_(400970, "sum_2", lambda: sum_2))
        _l_(400972)
        _c_(400977, _n_(400973, "print", lambda: print), _c_(400976, _n_(400974, "max", lambda: max), _n_(400975, "sum_2", lambda: sum_2)))
        _l_(400978)

s=_n_(400981, "Solution", lambda: Solution)
_l_(400982)
q=[-2,1,-3,4,-1,2,1,-5,4]
_l_(400983)

_c_(400987, _a_(400985, _n_(400984, "s", lambda: s), "maxSubArray"), 'w',_n_(400986, "q", lambda: q))
_l_(400988)