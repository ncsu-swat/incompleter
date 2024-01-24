# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61823343/typeerror-python-ask-to-insert-self-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class debugger():
    _l_(444230)

    def __init__(self, state=False):
        _l_(444192)

        _n_(444189, "self", lambda: self).state = _n_(444190, "state", lambda: state)
        _l_(444191)

    def status(self, inp:_n_(444193, "bool", lambda: bool)):
        _l_(444217)

        if _n_(444194, "inp", lambda: inp) == True and _a_(444196, _n_(444195, "self", lambda: self), "state") == False:
            _l_(444213)

_c_(444198, _n_(444197, "print", lambda: print), 'Debugger activated')        elif _n_(444199, "inp", lambda: inp) == True and _a_(444201, _n_(444200, "self", lambda: self), "state") == True:
            _l_(444212)

_c_(444203, _n_(444202, "print", lambda: print), 'Debugger alredy started')        elif _n_(444204, "inp", lambda: inp) == False and _a_(444206, _n_(444205, "self", lambda: self), "state") == True:
            _l_(444211)

_c_(444208, _n_(444207, "print", lambda: print), 'Debugger stopped')        else: _c_(444210, _n_(444209, "print", lambda: print), 'Debugger alredy stopped')
        _n_(444214, "self", lambda: self).state = _n_(444215, "inp", lambda: inp)
        _l_(444216)

    def log(self, msg:_n_(444218, "str", lambda: str)):
        _l_(444225)

        if _a_(444220, _n_(444219, "self", lambda: self), "state") == True:
            _l_(444224)

_c_(444223, _n_(444221, "print", lambda: print), f'[DEBUGGER]: {_n_(444222, "msg", lambda: msg)}')        else: pass

    def __repr__(self):
        _l_(444229)

        if _a_(444227, _n_(444226, 'self', lambda: self), 'state') == True:
            _l_(444228)

return 'Debugger status: Active'        else: return 'Debugger status: Disabled'

_c_(444233, _a_(444232, _n_(444231, 'debugger', lambda: debugger), 'status'), True)
_l_(444234)
_c_(444236, _n_(444235, 'debugger', lambda: debugger))
_l_(444237)
_c_(444240, _a_(444239, _n_(444238, 'debugger', lambda: debugger), 'log'), 'Test from debugger')
_l_(444241)