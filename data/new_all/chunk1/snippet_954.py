# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67447825/while-using-automl-from-evalml-getting-error-attributeerror-datatable-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_a_(387559, _n_(387558, "df", lambda: df), "loc")[(_a_(387561, _n_(387560, "df", lambda: df), "quality")<6), 'flag_class'] = 1
_l_(387562)
_a_(387564, _n_(387563, "df", lambda: df), "loc")[(_a_(387566, _n_(387565, "df", lambda: df), "quality")==6), 'flag_class'] = 2
_l_(387567)
_a_(387569, _n_(387568, "df", lambda: df), "loc")[(_a_(387571, _n_(387570, "df", lambda: df), "quality")>6), 'flag_class'] = 3
_l_(387572)