# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(97704)

except ImportError:
    pass
try:
    from dateutil.parser import parse
    _l_(97706)

except ImportError:
    pass
_c_(97708, _n_(97707, "print", lambda: print), 'Convert datatime to strings:')
_l_(97709)
_c_(97714, _n_(97710, "print", lambda: print), _c_(97713, _a_(97712, _n_(97711, "stamp", lambda: stamp), "strftime"), '%Y-%m-%d'))
_l_(97715)
_c_(97720, _n_(97716, "print", lambda: print), _c_(97719, _a_(97718, _n_(97717, "stamp", lambda: stamp), "strftime"), '%d/%b/%y'))
_l_(97721)
_c_(97723, _n_(97722, "print", lambda: print), '\nConvert strings to datatime:')
_l_(97724)
_c_(97728, _n_(97725, "print", lambda: print), _c_(97727, _n_(97726, "parse", lambda: parse), 'Sept 17th 2019'))
_l_(97729)
_c_(97733, _n_(97730, "print", lambda: print), _c_(97732, _n_(97731, "parse", lambda: parse), '1/11/2019'))
_l_(97734)
_c_(97738, _n_(97735, "print", lambda: print), _c_(97737, _n_(97736, "parse", lambda: parse), '1/11/2019', dayfirst=True))
_l_(97739)