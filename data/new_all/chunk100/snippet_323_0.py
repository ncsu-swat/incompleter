# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(s):
    _l_(31209)

    messg = []
    _l_(31159)
    if not _c_(31165, _n_(31160, "any", lambda: any), (_c_(31163, _a_(31162, _n_(31161, "x", lambda: x), "isupper")) for x in _n_(31164, "s", lambda: s))):
        _l_(31170)

        _c_(31168, _a_(31167, _n_(31166, "messg", lambda: messg), "append"), 'String must have 1 upper case character.')
        _l_(31169)
    if not _c_(31176, _n_(31171, "any", lambda: any), (_c_(31174, _a_(31173, _n_(31172, "x", lambda: x), "islower")) for x in _n_(31175, "s", lambda: s))):
        _l_(31181)

        _c_(31179, _a_(31178, _n_(31177, "messg", lambda: messg), "append"), 'String must have 1 lower case character.')
        _l_(31180)
    if not _c_(31187, _n_(31182, "any", lambda: any), (_c_(31185, _a_(31184, _n_(31183, "x", lambda: x), "isdigit")) for x in _n_(31186, "s", lambda: s))):
        _l_(31192)

        _c_(31190, _a_(31189, _n_(31188, "messg", lambda: messg), "append"), 'String must have 1 number.')
        _l_(31191)
    if _c_(31195, _n_(31193, "len", lambda: len), _n_(31194, "s", lambda: s)) < 8:
        _l_(31200)

        _c_(31198, _a_(31197, _n_(31196, "messg", lambda: messg), "append"), 'String length should be atleast 8.')
        _l_(31199)
    if not _n_(31201, "messg", lambda: messg):
        _l_(31206)

        _c_(31204, _a_(31203, _n_(31202, "messg", lambda: messg), "append"), 'Valid string.')
        _l_(31205)
    aux = _n_(31207, "messg", lambda: messg)
    _l_(31208)
    return aux
_c_(31214, _n_(31210, "print", lambda: print), _c_(31213, _n_(31211, "check_string", lambda: check_string), _n_(31212, "s", lambda: s)))
_l_(31215)