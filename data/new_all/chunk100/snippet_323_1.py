# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(s):
    _l_(31265)

    if not _c_(31221, _n_(31216, "any", lambda: any), (_c_(31219, _a_(31218, _n_(31217, "x", lambda: x), "isupper")) for x in _n_(31220, "s", lambda: s))):
        _l_(31226)

        _c_(31224, _a_(31223, _n_(31222, "messg", lambda: messg), "append"), 'String must have 1 upper case character.')
        _l_(31225)
    if not _c_(31232, _n_(31227, "any", lambda: any), (_c_(31230, _a_(31229, _n_(31228, "x", lambda: x), "islower")) for x in _n_(31231, "s", lambda: s))):
        _l_(31237)

        _c_(31235, _a_(31234, _n_(31233, "messg", lambda: messg), "append"), 'String must have 1 lower case character.')
        _l_(31236)
    if not _c_(31243, _n_(31238, "any", lambda: any), (_c_(31241, _a_(31240, _n_(31239, "x", lambda: x), "isdigit")) for x in _n_(31242, "s", lambda: s))):
        _l_(31248)

        _c_(31246, _a_(31245, _n_(31244, "messg", lambda: messg), "append"), 'String must have 1 number.')
        _l_(31247)
    if _c_(31251, _n_(31249, "len", lambda: len), _n_(31250, "s", lambda: s)) < 8:
        _l_(31256)

        _c_(31254, _a_(31253, _n_(31252, "messg", lambda: messg), "append"), 'String length should be atleast 8.')
        _l_(31255)
    if not _n_(31257, "messg", lambda: messg):
        _l_(31262)

        _c_(31260, _a_(31259, _n_(31258, "messg", lambda: messg), "append"), 'Valid string.')
        _l_(31261)
    aux = _n_(31263, "messg", lambda: messg)
    _l_(31264)
    return aux
s = _c_(31267, _n_(31266, "input", lambda: input), 'Input the string: ')
_l_(31268)
_c_(31273, _n_(31269, "print", lambda: print), _c_(31272, _n_(31270, "check_string", lambda: check_string), _n_(31271, "s", lambda: s)))
_l_(31274)