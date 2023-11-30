# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sec_to_hours(seconds):
    _l_(1538210)

    a=_c_(1538192, _n_(1538190, "str", lambda: str), _n_(1538191, "seconds", lambda: seconds)//3600)
    _l_(1538193)
    b=_c_(1538196, _n_(1538194, "str", lambda: str), (_n_(1538195, "seconds", lambda: seconds)%3600)//60)
    _l_(1538197)
    c=_c_(1538200, _n_(1538198, "str", lambda: str), (_n_(1538199, "seconds", lambda: seconds)%3600)%60)
    _l_(1538201)
    d=[_c_(1538206, _a_(1538202, "{} hours {} mins {} seconds", "format"), _n_(1538203, "a", lambda: a), _n_(1538204, "b", lambda: b), _n_(1538205, "c", lambda: c))]
    _l_(1538207)
    aux = _n_(1538208, "d", lambda: d)
    _l_(1538209)
    return aux


_c_(1538214, _n_(1538211, "print", lambda: print), _c_(1538213, _n_(1538212, "sec_to_hours", lambda: sec_to_hours), 10000))
_l_(1538215)
# ['2 hours 46 mins 40 seconds']

_c_(1538219, _n_(1538216, "print", lambda: print), _c_(1538218, _n_(1538217, "sec_to_hours", lambda: sec_to_hours), 60*60*24+105))
_l_(1538220)
# ['24 hours 1 mins 45 seconds']

