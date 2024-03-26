# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(s):
    _l_(110615)

    messg = []
    _l_(110565)
    if not _c_(110571, _n_(110566, "any", lambda: any), (_c_(110569, _a_(110568, _n_(110567, "x", lambda: x), "isupper")) for x in _n_(110570, "s", lambda: s))):
        _l_(110576)

        _c_(110574, _a_(110573, _n_(110572, "messg", lambda: messg), "append"), 'String must have 1 upper case character.')
        _l_(110575)
    if not _c_(110582, _n_(110577, "any", lambda: any), (_c_(110580, _a_(110579, _n_(110578, "x", lambda: x), "islower")) for x in _n_(110581, "s", lambda: s))):
        _l_(110587)

        _c_(110585, _a_(110584, _n_(110583, "messg", lambda: messg), "append"), 'String must have 1 lower case character.')
        _l_(110586)
    if not _c_(110593, _n_(110588, "any", lambda: any), (_c_(110591, _a_(110590, _n_(110589, "x", lambda: x), "isdigit")) for x in _n_(110592, "s", lambda: s))):
        _l_(110598)

        _c_(110596, _a_(110595, _n_(110594, "messg", lambda: messg), "append"), 'String must have 1 number.')
        _l_(110597)
    if _c_(110601, _n_(110599, "len", lambda: len), _n_(110600, "s", lambda: s)) < 8:
        _l_(110606)

        _c_(110604, _a_(110603, _n_(110602, "messg", lambda: messg), "append"), 'String length should be atleast 8.')
        _l_(110605)
    if not _n_(110607, "messg", lambda: messg):
        _l_(110612)

        _c_(110610, _a_(110609, _n_(110608, "messg", lambda: messg), "append"), 'Valid string.')
        _l_(110611)
    aux = _n_(110613, "messg", lambda: messg)
    _l_(110614)
    return aux
_c_(110620, _n_(110616, "print", lambda: print), _c_(110619, _n_(110617, "check_string", lambda: check_string), _n_(110618, "s", lambda: s)))
_l_(110621)