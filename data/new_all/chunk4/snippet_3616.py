# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71251272/typeerror-type-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from msilib import make_id
    _l_(639808)

except ImportError:
    pass
try:
    from tkinter import simpledialog,Tk
    _l_(639810)

except ImportError:
    pass
def number():
    _l_(639814)

    win = _c_(639812, _n_(639811, "make_id", lambda: make_id), '')
    _l_(639813)
def winner_number():
    _l_(639816)

    numberd = 'c4'
    _l_(639815)
def get_task():
    _l_(639823)

    task=_c_(639819, _a_(639818, _n_(639817, "simpledialog", lambda: simpledialog), "askstring"), "id製造器",'你要製造id嗎?')
    _l_(639820)
    aux = _n_(639821, "task", lambda: task)
    _l_(639822)
    return aux
def get_message():
    _l_(639832)

    message=_c_(639828, _a_(639825, _n_(639824, "simpledialog", lambda: simpledialog), "askstring"), '你的id是:',_n_(639826, "number", lambda: number),'中獎號碼:',_n_(639827, "winner_number", lambda: winner_number))
    _l_(639829)
    aux = _n_(639830, "message", lambda: message)
    _l_(639831)
    return aux
screen = _c_(639834, _n_(639833, "Tk", lambda: Tk))
_l_(639835)

while True:
    _l_(639860)

    task=_c_(639837, _n_(639836, "get_task", lambda: get_task))
    _l_(639838)
    if _n_(639839, "task", lambda: task) == "要":
        _l_(639859)

        massage= _n_(639840, "get_message", lambda: get_message)
        _l_(639841)
        number = _n_(639842, "make_id", lambda: make_id)
        _l_(639843)
        if _c_(639846, _n_(639844, "number", lambda: number), _n_(639845, "str", lambda: str)) in _c_(639848, _n_(639847, "winner_number", lambda: winner_number)):
            _l_(639852)

            _c_(639850, _n_(639849, "print", lambda: print), '你的運氣超好!!')
            _l_(639851)
    elif _n_(639853, "task", lambda: task)=='cancel':
        _l_(639858)

        _c_(639855, _n_(639854, "print", lambda: print), '你失敗了!!')
        _l_(639856)
    else:
        break
        _l_(639857)