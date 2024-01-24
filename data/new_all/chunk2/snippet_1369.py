# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68415092/i-cant-understand-why-googletrans-in-python-isnt-working-it-gives-error-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from googletrans import Translator
    _l_(427974)

except ImportError:
    pass

translator = _c_(427976, _n_(427975, "Translator", lambda: Translator)) 
_l_(427977) 

result = _c_(427980, _a_(427979, _n_(427978, "translator", lambda: translator), "translate"), 'Mikä on nimesi', src='fi', dest='fr')
_l_(427981)

_c_(427985, _n_(427982, "print", lambda: print), _a_(427984, _n_(427983, "result", lambda: result), "src"))
_l_(427986)
 
_c_(427990, _n_(427987, "print", lambda: print), _a_(427989, _n_(427988, "result", lambda: result), "dest"))
_l_(427991)
 
_c_(427995, _n_(427992, "print", lambda: print), _a_(427994, _n_(427993, "result", lambda: result), "text"))
_l_(427996)