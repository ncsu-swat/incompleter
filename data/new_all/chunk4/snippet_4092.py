# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63044360/receiving-type-error-when-comparing-two-variables-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(583779)

except ImportError:
    pass

list = [1,2,3,4,2323449,1,525]
_l_(583780)

def Search(arr):
    _l_(583880)

    # sorting
    i = 0
    _l_(583781)
    _c_(583784, _n_(583782, "print", lambda: print), f"Given list: {_n_(583783, 'list', lambda: list)}")
    _l_(583785)
    _c_(583787, _n_(583786, "print", lambda: print), "Sorting...")
    _l_(583788)
    _c_(583791, _a_(583790, _n_(583789, "time", lambda: time), "sleep"), 1.75)
    _l_(583792)
    for i in _c_(583797, _n_(583793, "range", lambda: range), _c_(583796, _n_(583794, "len", lambda: len), _n_(583795, "list", lambda: list))):
        _l_(583820)

        if _n_(583798, "i", lambda: i) + 1 >= _c_(583801, _n_(583799, "len", lambda: len), _n_(583800, "list", lambda: list)):
            _l_(583819)

            break
            _l_(583802)
        elif  _n_(583803, "list", lambda: list)[_n_(583804, "i", lambda: i) + 1] < _n_(583805, "list", lambda: list)[_n_(583806, "i", lambda: i)]:
            _l_(583818)

            _c_(583809, _a_(583808, _n_(583807, "list", lambda: list), "sort"))
            _l_(583810)
            _c_(583812, _n_(583811, "print", lambda: print), "List has been sorted ")
            _l_(583813)
            _c_(583816, _n_(583814, "print", lambda: print), f"Sorted list: {_n_(583815, 'list', lambda: list)}")
            _l_(583817)
    #---------------------------------------
    # searching
    inputCheck = True
    _l_(583821)
    while _n_(583822, "inputCheck", lambda: inputCheck):
        _l_(583842)

        n = _c_(583824, _n_(583823, "input", lambda: input), "Enter a number to find in the list: ")
        _l_(583825)
        try:
            _l_(583841)

            _c_(583828, _n_(583826, "int", lambda: int), _n_(583827, "n", lambda: n))
            _l_(583829)
            inputCheck = False                                                                                                                                                                                            
            _l_(583830)                                                                                                                                                                                            
        except _n_(583831, "ValueError", lambda: ValueError) or _n_(583832, "TypeError", lambda: TypeError):
            _l_(583840)

            _c_(583834, _n_(583833, "print", lambda: print), "Please enter a number")
            _l_(583835)
            _c_(583838, _a_(583837, _n_(583836, "time", lambda: time), "sleep"), 0.6)
            _l_(583839)



    _c_(583844, _n_(583843, "print", lambda: print), "Searching...")
    _l_(583845)

    l = 0
    _l_(583846)
    h = _c_(583849, _n_(583847, "len", lambda: len), _n_(583848, "list", lambda: list)) - 1 
    _l_(583850) 

    while _n_(583851, "l", lambda: l) <= _n_(583852, "h", lambda: h):
        _l_(583879)

        mid = (_n_(583853, "l", lambda: l) + _n_(583854, "h", lambda: h)) // 2
        _l_(583855)

        if _n_(583856, "list", lambda: list)[_n_(583857, "mid", lambda: mid)] == _n_(583858, "n", lambda: n):
            _l_(583878)

            pos = _n_(583859, "mid", lambda: mid)
            _l_(583860)
            _c_(583863, _n_(583861, "print", lambda: print), f"Found at index {_n_(583862, 'pos', lambda: pos)}")
            _l_(583864)
            break
            _l_(583865)
        else:
            _c_(583868, _n_(583866, "print", lambda: print), _n_(583867, "n", lambda: n))
            _l_(583869)
            if _n_(583870, "list", lambda: list)[_n_(583871, "mid", lambda: mid)] < _n_(583872, "n", lambda: n):
                _l_(583877)

                l = _n_(583873, "mid", lambda: mid)
                _l_(583874)
            else:
                h = _n_(583875, "mid", lambda: mid)
                _l_(583876)
            
_c_(583883, _n_(583881, "Search", lambda: Search), _n_(583882, "list", lambda: list))
_l_(583884)