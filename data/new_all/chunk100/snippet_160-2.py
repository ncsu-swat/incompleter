# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_chars(str1, unwanted_chars):
    _l_(102926)

    for i in _n_(102917, "unwanted_chars", lambda: unwanted_chars):
        _l_(102923)

        str1 = _c_(102921, _a_(102919, _n_(102918, "str1", lambda: str1), "replace"), _n_(102920, "i", lambda: i), '')
        _l_(102922)
    aux = _n_(102924, "str1", lambda: str1)
    _l_(102925)
    return aux
str1 = 'Pyth*^on Exercis^es'
_l_(102927)
str2 = 'A%^!B#*CD'
_l_(102928)
_c_(102931, _n_(102929, "print", lambda: print), 'Original String : ' + _n_(102930, "str1", lambda: str1))
_l_(102932)
_c_(102934, _n_(102933, "print", lambda: print), 'After removing unwanted characters:')
_l_(102935)
_c_(102941, _n_(102936, "print", lambda: print), _c_(102940, _n_(102937, "remove_chars", lambda: remove_chars), _n_(102938, "str1", lambda: str1), _n_(102939, "unwanted_chars", lambda: unwanted_chars)))
_l_(102942)
_c_(102945, _n_(102943, "print", lambda: print), '\nOriginal String : ' + _n_(102944, "str2", lambda: str2))
_l_(102946)
_c_(102948, _n_(102947, "print", lambda: print), 'After removing unwanted characters:')
_l_(102949)
_c_(102955, _n_(102950, "print", lambda: print), _c_(102954, _n_(102951, "remove_chars", lambda: remove_chars), _n_(102952, "str2", lambda: str2), _n_(102953, "unwanted_chars", lambda: unwanted_chars)))
_l_(102956)