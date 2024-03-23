# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def wiggle_sort(arra_nums):
    _l_(70003)

    for (i, _) in _c_(69984, _n_(69982, "enumerate", lambda: enumerate), _n_(69983, "arra_nums", lambda: arra_nums)):
        _l_(70000)

        if (_n_(69985, "i", lambda: i) % 2 == 1) == (_n_(69986, "arra_nums", lambda: arra_nums)[_n_(69987, "i", lambda: i) - 1] > _n_(69988, "arra_nums", lambda: arra_nums)[_n_(69989, "i", lambda: i)]):
            _l_(69999)

            (_n_(69990, "arra_nums", lambda: arra_nums)[_n_(69991, "i", lambda: i) - 1], _n_(69992, "arra_nums", lambda: arra_nums)[_n_(69993, "i", lambda: i)]) = (_n_(69994, "arra_nums", lambda: arra_nums)[_n_(69995, "i", lambda: i)], _n_(69996, "arra_nums", lambda: arra_nums)[_n_(69997, "i", lambda: i) - 1])
            _l_(69998)
    aux = _n_(70001, "arra_nums", lambda: arra_nums)
    _l_(70002)
    return aux
_c_(70005, _n_(70004, "print", lambda: print), 'Input the array elements: ')
_l_(70006)
_c_(70008, _n_(70007, "print", lambda: print), 'Original unsorted array:')
_l_(70009)
_c_(70012, _n_(70010, "print", lambda: print), _n_(70011, "arra_nums", lambda: arra_nums))
_l_(70013)
_c_(70015, _n_(70014, "print", lambda: print), 'The said array after applying Wiggle sort:')
_l_(70016)
_c_(70021, _n_(70017, "print", lambda: print), _c_(70020, _n_(70018, "wiggle_sort", lambda: wiggle_sort), _n_(70019, "arra_nums", lambda: arra_nums)))
_l_(70022)