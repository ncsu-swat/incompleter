# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63044360/receiving-type-error-when-comparing-two-variables-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(604874)

except ImportError:
    pass

list = [1,2,3,4,2323449,1,525]
_l_(604875)

def Search(arr):
    _l_(604975)

    # sorting
    i = 0
    _l_(604876)
    _c_(604879, _n_(604877, "print", lambda: print), f"Given list: {_n_(604878, 'list', lambda: list)}")
    _l_(604880)
    _c_(604882, _n_(604881, "print", lambda: print), "Sorting...")
    _l_(604883)
    _c_(604886, _a_(604885, _n_(604884, "time", lambda: time), "sleep"), 1.75)
    _l_(604887)
    for i in _c_(604892, _n_(604888, "range", lambda: range), _c_(604891, _n_(604889, "len", lambda: len), _n_(604890, "list", lambda: list))):
        _l_(604915)

        if _n_(604893, "i", lambda: i) + 1 >= _c_(604896, _n_(604894, "len", lambda: len), _n_(604895, "list", lambda: list)):
            _l_(604914)

            break
            _l_(604897)
        elif  _n_(604898, "list", lambda: list)[_n_(604899, "i", lambda: i) + 1] < _n_(604900, "list", lambda: list)[_n_(604901, "i", lambda: i)]:
            _l_(604913)

            _c_(604904, _a_(604903, _n_(604902, "list", lambda: list), "sort"))
            _l_(604905)
            _c_(604907, _n_(604906, "print", lambda: print), "List has been sorted ")
            _l_(604908)
            _c_(604911, _n_(604909, "print", lambda: print), f"Sorted list: {_n_(604910, 'list', lambda: list)}")
            _l_(604912)
    #---------------------------------------
    # searching
    inputCheck = True
    _l_(604916)
    while _n_(604917, "inputCheck", lambda: inputCheck):
        _l_(604937)

        n = _c_(604919, _n_(604918, "input", lambda: input), "Enter a number to find in the list: ")
        _l_(604920)
        try:
            _l_(604936)

            _c_(604923, _n_(604921, "int", lambda: int), _n_(604922, "n", lambda: n))
            _l_(604924)
            inputCheck = False                                                                                                                                                                                            
            _l_(604925)                                                                                                                                                                                            
        except _n_(604926, "ValueError", lambda: ValueError) or _n_(604927, "TypeError", lambda: TypeError):
            _l_(604935)

            _c_(604929, _n_(604928, "print", lambda: print), "Please enter a number")
            _l_(604930)
            _c_(604933, _a_(604932, _n_(604931, "time", lambda: time), "sleep"), 0.6)
            _l_(604934)



    _c_(604939, _n_(604938, "print", lambda: print), "Searching...")
    _l_(604940)

    l = 0
    _l_(604941)
    h = _c_(604944, _n_(604942, "len", lambda: len), _n_(604943, "list", lambda: list)) - 1 
    _l_(604945) 

    while _n_(604946, "l", lambda: l) <= _n_(604947, "h", lambda: h):
        _l_(604974)

        mid = (_n_(604948, "l", lambda: l) + _n_(604949, "h", lambda: h)) // 2
        _l_(604950)

        if _n_(604951, "list", lambda: list)[_n_(604952, "mid", lambda: mid)] == _n_(604953, "n", lambda: n):
            _l_(604973)

            pos = _n_(604954, "mid", lambda: mid)
            _l_(604955)
            _c_(604958, _n_(604956, "print", lambda: print), f"Found at index {_n_(604957, 'pos', lambda: pos)}")
            _l_(604959)
            break
            _l_(604960)
        else:
            _c_(604963, _n_(604961, "print", lambda: print), _n_(604962, "n", lambda: n))
            _l_(604964)
            if _n_(604965, "list", lambda: list)[_n_(604966, "mid", lambda: mid)] < _n_(604967, "n", lambda: n):
                _l_(604972)

                l = _n_(604968, "mid", lambda: mid)
                _l_(604969)
            else:
                h = _n_(604970, "mid", lambda: mid)
                _l_(604971)
            
_c_(604978, _n_(604976, "Search", lambda: Search), _n_(604977, "list", lambda: list))
_l_(604979)