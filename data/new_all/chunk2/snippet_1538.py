# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38986341/python-nameerror-name-is-not-defined-related-to-having-default-input-argument
#-------------------------------------------------------------------
#EXAMPLES:
#-------------------------------------------------------------------
#Only executute this block of code if running this module directly,
#*not* if importing it
#-see here: http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(438689, "__name__", lambda: __name__) == "__main__":
    _l_(438763)

    try:
        import random
        _l_(438691)

    except ImportError:
        pass
    _c_(438694, _a_(438693, _n_(438692, "random", lambda: random), "seed"), 0)
    _l_(438695)

    bytes = _c_(438697, _n_(438696, "bytearray", lambda: bytearray), 100)
    _l_(438698)
    for i in _c_(438703, _n_(438699, "range", lambda: range), _c_(438702, _n_(438700, "len", lambda: len), _n_(438701, "bytes", lambda: bytes))):
        _l_(438712)

        _n_(438704, "bytes", lambda: bytes)[_n_(438705, "i", lambda: i)] = _c_(438710, _n_(438706, "int", lambda: int), _c_(438709, _a_(438708, _n_(438707, "random", lambda: random), "random"))*256)
        _l_(438711)

    _c_(438717, _n_(438713, "print", lambda: print), _c_(438716, _n_(438714, "list", lambda: list), _n_(438715, "bytes", lambda: bytes))); _c_(438719, _n_(438718, "print", lambda: print));
    _l_(438720)

    _c_(438722, _n_(438721, "print", lambda: print), 'built-in method:')
    _l_(438723)
    _c_(438728, _n_(438724, "print", lambda: print), _c_(438727, _a_(438726, _n_(438725, "bytes", lambda: bytes), "find"), 255))
    _l_(438729)
    _c_(438734, _n_(438730, "print", lambda: print), _c_(438733, _a_(438732, _n_(438731, "bytes", lambda: bytes), "find"), 2,10,97))
    _l_(438735)
    _c_(438740, _n_(438736, "print", lambda: print), _c_(438739, _a_(438738, _n_(438737, "bytes", lambda: bytes), "find"), 5,97,4))
    _l_(438741)

    _c_(438743, _n_(438742, "print", lambda: print), '\ncircularFind:')
    _l_(438744)
    _c_(438749, _n_(438745, "print", lambda: print), _c_(438748, _n_(438746, "circularFind", lambda: circularFind), _n_(438747, "bytes", lambda: bytes),255))
    _l_(438750)
    _c_(438755, _n_(438751, "print", lambda: print), _c_(438754, _n_(438752, "circularFind", lambda: circularFind), _n_(438753, "bytes", lambda: bytes),2,10,97))
    _l_(438756)
    _c_(438761, _n_(438757, "print", lambda: print), _c_(438760, _n_(438758, "circularFind", lambda: circularFind), _n_(438759, "bytes", lambda: bytes),5,97,4))
    _l_(438762)