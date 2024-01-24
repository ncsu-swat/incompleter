# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/16567713/fixed-python-nameerror-fixed-attributeerror-and-got-this
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import *
    _l_(538722)

except ImportError:
    pass
try:
    from xml.dom import minidom
    _l_(538724)

except ImportError:
    pass
try:
    import parser
    _l_(538726)

except ImportError:
    pass
try:
    from parser import *
    _l_(538728)

except ImportError:
    pass
_c_(538730, _n_(538729, "print", lambda: print), "+---+ Roleplay Stat Reader +---+")
_l_(538731)
_c_(538733, _n_(538732, "print", lambda: print), "Load previous DAT file, or create new one (new/load file)")
_l_(538734)
IN=_c_(538736, _n_(538735, "input", lambda: input))
_l_(538737)
splt = _c_(538740, _a_(538739, _n_(538738, "IN", lambda: IN), "split"), ' ')
_l_(538741)
if _n_(538742, "splt", lambda: splt)[0]=="new":
    _l_(538758)

    _c_(538745, _n_(538743, "xmlwrite", lambda: xmlwrite), _n_(538744, "splt", lambda: splt)[1])
    _l_(538746)
else:
    if _c_(538749, _n_(538747, "len", lambda: len), _n_(538748, "splt", lambda: splt)[1])<2:
        _l_(538757)

        _c_(538751, _n_(538750, "print", lambda: print), "err")
        _l_(538752)
    else:
        _c_(538755, _n_(538753, "xmlread", lambda: xmlread), _n_(538754, "splt", lambda: splt)[1])
        _l_(538756)
ex=_c_(538760, _n_(538759, "input", lambda: input), "Press ENTER to Exit...")
_l_(538761)