# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53809815/typeerror-unsupported-operand-types-for-sub-str-and-int-on-line-8
#Define payment, knowing that up to 40 hours it is normal rate, and above that every hour is paid at 150%.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
totalHours = _c_(693670, _n_(693669, "input", lambda: input), "Enter the total amount of worked hours:\n")
_l_(693671)
hourlyWage = _c_(693673, _n_(693672, "input", lambda: input), "Enter the payrate per hour:\n")
_l_(693674)
if _n_(693675, "totalHours", lambda: totalHours) <= 40:
    _l_(693690)

    regularHours = _n_(693676, "totalHours", lambda: totalHours)
    _l_(693677)
    overtime = 0
    _l_(693678)
else:
    overtime = _c_(693683, _n_(693679, "float", lambda: float), _c_(693682, _n_(693680, "input", lambda: input), _n_(693681, "totalHours", lambda: totalHours) - 40))
    _l_(693684)
    regularHours = _c_(693688, _n_(693685, "float", lambda: float), _c_(693687, _n_(693686, "input", lambda: input), 40))
    _l_(693689)
payment = _n_(693691, "hourlyWage", lambda: hourlyWage)*_n_(693692, "regularHours", lambda: regularHours) + (1.5*_n_(693693, "hourlyWage", lambda: hourlyWage))*_n_(693694, "overtime", lambda: overtime)
_l_(693695)
_c_(693698, _n_(693696, "print", lambda: print), _n_(693697, "payment", lambda: payment))
_l_(693699)