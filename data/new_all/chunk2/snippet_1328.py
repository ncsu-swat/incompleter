# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42122240/sqlite-typeerror-query-takes-2-positional-arguments-but-4-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from db_manage import inv_enq
    _l_(425776)

except ImportError:
    pass

def main():
    _l_(425788)

    ord_numb = _c_(425778, _n_(425777, "input", lambda: input), 'Enter Order Number > ')
    _l_(425779)
    part_numb = _c_(425781, _n_(425780, "input", lambda: input), 'Enter Part Number > ')
    _l_(425782)
    _c_(425786, _n_(425783, "inv_enq", lambda: inv_enq), _n_(425784, "ord_numb", lambda: ord_numb), _n_(425785, "part_numb", lambda: part_numb))
    _l_(425787)

if _n_(425789, "__name__", lambda: __name__) == "__main__":
    _l_(425793)

    _c_(425791, _n_(425790, "main", lambda: main))
    _l_(425792)