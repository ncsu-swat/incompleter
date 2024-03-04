# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7065164/how-to-make-a-timezone-aware-datetime-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
unaware=_c_(62518, _a_(62517, _n_(62516, "parser", lambda: parser), "parse"), "2020-05-01 0:00:00")
_l_(62519)
aware=_c_(62530, _a_(62526, _c_(62525, _a_(62521, _n_(62520, "unaware", lambda: unaware), "replace"), tzinfo=_c_(62524, _a_(62523, _n_(62522, "tz", lambda: tz), "tzlocal"))), "astimezone"), _c_(62529, _a_(62528, _n_(62527, "tz", lambda: tz), "tzlocal")))
_l_(62531)

