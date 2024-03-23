# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53809815/typeerror-unsupported-operand-types-for-sub-str-and-int-on-line-8
#Define payment, knowing that up to 40 hours it is normal rate, and above that every hour is paid at 150%.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
totalHours = _c_(702541, _n_(702540, "input", lambda: input), "Enter the total amount of worked hours:\n")
_l_(702542)
hourlyWage = _c_(702544, _n_(702543, "input", lambda: input), "Enter the payrate per hour:\n")
_l_(702545)
if _n_(702546, "totalHours", lambda: totalHours) <= 40:
    _l_(702561)

    regularHours = _n_(702547, "totalHours", lambda: totalHours)
    _l_(702548)
    overtime = 0
    _l_(702549)
else:
    overtime = _c_(702554, _n_(702550, "float", lambda: float), _c_(702553, _n_(702551, "input", lambda: input), _n_(702552, "totalHours", lambda: totalHours) - 40))
    _l_(702555)
    regularHours = _c_(702559, _n_(702556, "float", lambda: float), _c_(702558, _n_(702557, "input", lambda: input), 40))
    _l_(702560)
payment = _n_(702562, "hourlyWage", lambda: hourlyWage)*_n_(702563, "regularHours", lambda: regularHours) + (1.5*_n_(702564, "hourlyWage", lambda: hourlyWage))*_n_(702565, "overtime", lambda: overtime)
_l_(702566)
_c_(702569, _n_(702567, "print", lambda: print), _n_(702568, "payment", lambda: payment))
_l_(702570)