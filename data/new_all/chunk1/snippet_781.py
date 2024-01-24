# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53465931/string-concatenate-typeerror-can-only-concatenate-str-not-int-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
salaries = {'John':'20','Sally':'30','Sammy':'15'}
_l_(388254)
_c_(388257, _n_(388255, "print", lambda: print), _n_(388256, "salaries", lambda: salaries)['John'])
_l_(388258)

_n_(388259, "salaries", lambda: salaries)['John'] = _n_(388260, "salaries", lambda: salaries)['John'] + 30
_l_(388261)
_c_(388264, _n_(388262, "print", lambda: print), _n_(388263, "salaries", lambda: salaries)['John'])
_l_(388265)