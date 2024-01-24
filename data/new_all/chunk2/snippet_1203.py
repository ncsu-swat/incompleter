# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44129593/typeerror-the-first-argument-must-be-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import schedule
    _l_(437769)

except ImportError:
    pass
try:
    import time
    _l_(437771)

except ImportError:
    pass

def rank():
    _l_(437782)

    try:
        import new_user as nu
        _l_(437773)

    except ImportError:
        pass
    _c_(437776, _a_(437775, _n_(437774, "nu", lambda: nu), "new_user"))  
    _l_(437777)  
    _c_(437779, _n_(437778, "print", lambda: print), 'successfully loaded')  
    _l_(437780)  
    aux = ""  
    _l_(437781)  
    return aux  

_c_(437790, _a_(437787, _a_(437786, _c_(437785, _a_(437784, _n_(437783, "schedule", lambda: schedule), "every"), 5), "minutes"), "do"), _c_(437789, _n_(437788, "rank", lambda: rank)))  
_l_(437791)  

while 1:
    _l_(437800)

    _c_(437794, _a_(437793, _n_(437792, "schedule", lambda: schedule), "run_pending"))  
    _l_(437795)  
    _c_(437798, _a_(437797, _n_(437796, "time", lambda: time), "sleep"), 1)  
    _l_(437799)  